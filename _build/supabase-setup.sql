-- Latitude Zero: story comments
-- Run once in the Supabase SQL editor of the project that will store comments.
-- New comments are hidden until you approve them (set approved = true).

create table if not exists public.comments (
  id          uuid primary key default gen_random_uuid(),
  post_slug   text not null check (char_length(post_slug) between 1 and 80),
  parent_id   uuid references public.comments(id) on delete cascade,
  name        text not null check (char_length(name) between 1 and 60),
  place       text check (place is null or char_length(place) <= 60),
  body        text not null check (char_length(body) between 1 and 1000),
  lang        text not null default 'en' check (lang in ('en','es')),
  hearts      integer not null default 0,
  is_team     boolean not null default false,  -- marks replies from Austin & Dennisse
  approved    boolean not null default false,
  created_at  timestamptz not null default now()
);

create index if not exists comments_post_idx on public.comments (post_slug, approved, created_at desc);

alter table public.comments enable row level security;

-- Anyone can read approved comments.
drop policy if exists "read approved comments" on public.comments;
create policy "read approved comments" on public.comments
  for select to anon, authenticated
  using (approved = true);

-- Anyone can submit a comment, but it always arrives unapproved, unhearted and not marked as the team.
drop policy if exists "submit comments for review" on public.comments;
create policy "submit comments for review" on public.comments
  for insert to anon, authenticated
  with check (approved = false and is_team = false and hearts = 0);

-- Hearts: a safe counter that only works on approved comments.
create or replace function public.heart_comment(comment_id uuid)
returns void
language sql
security definer
set search_path = public
as $$
  update public.comments set hearts = hearts + 1
  where id = comment_id and approved = true;
$$;

revoke all on function public.heart_comment(uuid) from public;
grant execute on function public.heart_comment(uuid) to anon, authenticated;

-- To approve: in Table Editor > comments, tick "approved" on a row.
-- To reply as the family: add a row with is_team = true, approved = true and parent_id set to the comment you're answering.

-- ============ Story reactions ============
create table if not exists public.reaction_totals (
  post_slug text not null check (char_length(post_slug) between 1 and 80),
  reaction  text not null check (reaction in ('love','same','go','wow')),
  total     integer not null default 0,
  primary key (post_slug, reaction)
);
alter table public.reaction_totals enable row level security;
-- no direct table access; everything goes through the functions below

create or replace function public.react(post text, new_reaction text, old_reaction text default null)
returns void language plpgsql security definer set search_path = public as $$
begin
  if new_reaction not in ('love','same','go','wow') or char_length(post) > 80 then return; end if;
  insert into reaction_totals(post_slug, reaction, total) values (post, new_reaction, 1)
    on conflict (post_slug, reaction) do update set total = reaction_totals.total + 1;
  if old_reaction in ('love','same','go','wow') and old_reaction <> new_reaction then
    update reaction_totals set total = greatest(total - 1, 0) where post_slug = post and reaction = old_reaction;
  end if;
end $$;

create or replace function public.reaction_counts(post text)
returns table(reaction text, total integer) language sql security definer set search_path = public stable as $$
  select reaction, total from reaction_totals where post_slug = post;
$$;

-- ============ Story polls ============
create table if not exists public.poll_totals (
  poll_id text not null check (char_length(poll_id) between 1 and 80),
  option  text not null check (char_length(option) between 1 and 40),
  total   integer not null default 0,
  primary key (poll_id, option)
);
alter table public.poll_totals enable row level security;

-- Allowed answers per poll (add a row for each new poll option you publish)
create table if not exists public.poll_options (
  poll_id text not null, option text not null, primary key (poll_id, option)
);
alter table public.poll_options enable row level security;
insert into public.poll_options values
  ('why-ecuador-abroad','planning'), ('why-ecuador-abroad','someday'), ('why-ecuador-abroad','following')
  on conflict do nothing;

create or replace function public.vote_poll(poll text, choice text)
returns void language plpgsql security definer set search_path = public as $$
begin
  if not exists (select 1 from poll_options where poll_id = poll and option = choice) then return; end if;
  insert into poll_totals(poll_id, option, total) values (poll, choice, 1)
    on conflict (poll_id, option) do update set total = poll_totals.total + 1;
end $$;

create or replace function public.poll_results(poll text)
returns table(option text, total integer) language sql security definer set search_path = public stable as $$
  select option, total from poll_totals where poll_id = poll;
$$;

revoke all on function public.react(text,text,text), public.reaction_counts(text), public.vote_poll(text,text), public.poll_results(text) from public;
grant execute on function public.react(text,text,text), public.reaction_counts(text), public.vote_poll(text,text), public.poll_results(text) to anon, authenticated;
