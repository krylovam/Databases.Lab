create_new_database = """

create extension if not exists dblink;
create or replace function create_database() returns void as $$
    begin
        if not exists (select from pg_database where datname = 'labdb') then
            perform dblink_exec(
                'dbname=postgres user=postgres password=1234567890',
                'create database labdb with owner newuser'
          );
        end if;
    end;
$$ language plpgsql;

create extension if not exists dblink;
create or replace function drop_database() returns void as $$
    begin
            perform dblink_exec(
                'dbname=postgres user=postgres password=1234567890',
                'drop database if exists labdb;'
            );
    end;
$$ language plpgsql;
"""

all_functions = """
CREATE TABLE if not exists NetflixShow
(
    id bigserial NOT NULL,
    name_show character varying(50) NOT NULL,
    country character varying(30),
    numberOfSeasons integer NOT NULL,
    numberOfEpisodes integer NOT NULL,
    watched integer NOT NULL,
    rest integer,
    PRIMARY KEY (id),
    UNIQUE (name_show)
);
create index if not exists name_show on NetflixShow(name_show);

CREATE TABLE if not exists Actors
(
    id bigserial NOT NULL,
    name_actor character varying(30) NOT NULL,
    showId bigserial NOT NULL,
    nameOfCharacter character varying(30) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (showId)
        REFERENCES NetflixShow (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    UNIQUE (name_actor)
);

create or replace function update_rest() returns trigger as $emp_stamp$
    BEGIN
        NEW.rest = NEW.numberOfSeasons * NEW.numberOfEpisodes - NEW.watched;
        return NEW;
    END;
$emp_stamp$ LANGUAGE plpgsql;

drop trigger if exists update_rest on NetflixShow;
create trigger update_rest
    before insert or update or delete on NetflixShow
for row execute procedure update_rest();
    end;


create or replace function truncate_actors() returns void as $$
    begin
        truncate Actors;
    end;
$$ language plpgsql;


create or replace function truncate_shows() returns void as $$
    begin
        truncate NetflixShow cascade;
    end;
$$ language plpgsql;

create or replace function add_actor(actor_name character varying, show_id bigint, 
                                         name_of_character character varying) returns void as $$
begin
    insert into Actors (name_actor, showId, nameOfCharacter) 
    values (actor_name, show_id, name_of_character);
    end;
$$ language plpgsql;

create or replace function add_show(show_name character varying, _country character varying,
                                    seasons integer, eps integer, _watched integer) returns void as $$
begin
    insert into NetflixShow (name_show, country, numberOfSeasons, numberOfEpisodes, watched) 
    values (show_name, _country, seasons, eps, _watched);
    end;
$$ language plpgsql;



create or replace function check_show(show_id bigint) returns json as $$
begin
    return (select json_agg(1) from NetflixShow where id = show_id);
    end;
$$ language plpgsql;

create or replace function check_actor(actor_id bigint) returns json as $$
begin
    return (select json_agg(1) from Actors where id = actor_id);
    end;
$$ language plpgsql;



create or replace function update_actor_name(_id bigint, new_name character varying) returns void as $$
begin
    update Actors set name_actor = new_name where id = _id;
    end;
$$ language plpgsql;


create or replace function update_actor_show(_id bigint, show_id bigint) returns void as $$
begin
    update Actors set showId = show_id where id = _id;
    end;
$$ language plpgsql;

create or replace function update_actor_charactername(_id bigint, characterName character varying ) returns void as $$
begin
    update Actors set nameOfCharacter = characterName where id = _id;
    end;
$$ language plpgsql;


create or replace function update_show_country(_id bigint, new_country character varying) returns void as $$
    declare output json;
begin
    update NetflixShow set country = new_country where id = _id;
    end;
$$ language plpgsql;

create or replace function update_show_seasons(_id bigint, num integer) returns void as $$
    declare output json;
begin
    update NetflixShow set numberOfSeasons = num where id = _id;
    end;
$$ language plpgsql;

create or replace function update_show_episodes(_id bigint, num integer) returns void as $$
    declare output json;
begin
    update NetflixShow set numberOfEpisodes = num where id = _id;
    end;
$$ language plpgsql;

create or replace function update_show_watched(_id bigint, num integer) returns void as $$
    declare output json;
begin
    update NetflixShow set watched = num where id = _id;
    end;
$$ language plpgsql;


create or replace function update_show_name(_show_id bigint, new_name character varying ) returns void as $$
begin 
    update NetflixShow set name_show = new_name where id = _show_id;
    end;
$$ language plpgsql;


create or replace function get_all_actors() returns json as $$
    begin
        return (select json_agg(s) from Actors s);
    end;
$$ language plpgsql;


create or replace function get_all_shows() returns json as $$
    begin
        return (select json_agg(s) from NetflixShow s);
    end;
$$ language plpgsql;


create or replace function get_actors_by_name(_name character varying) returns json as $$
    begin
        return (select json_agg(Actors) from Actors where name_actor = _name );
    end;
$$ language plpgsql;


create or replace function get_shows_by_country(_country character varying) returns json as $$
    begin
        return (select json_agg(NetflixShow) from NetflixShow where country = _country );
    end;
$$ language plpgsql;


create or replace function get_actors_by_show(show_id bigint) returns json as $$
    begin
        return (select json_agg(Actors) from Actors where showId = show_id );
    end;
$$ language plpgsql;

create or replace function get_actors_by_charactername(character_name character varying ) returns json as $$
    begin
        return (select json_agg(Actors) from Actors where nameOfCharacter = character_name );
    end;
$$ language plpgsql;


create or replace function get_shows_by_name(_name character varying ) returns json as $$
    begin
        return (select json_agg(NetflixShow) from NetflixShow where name_show = _name);
    end;
$$ language plpgsql;


create or replace function delete_actor(actor_id bigint) returns void as $$
    begin
        delete from Actors where id = actor_id;
    end;
$$ language plpgsql;


create or replace function delete_show(show_id bigint) returns void as $$
    begin
        delete from NetflixShow where id = show_id;
    end;
$$ language plpgsql;
"""