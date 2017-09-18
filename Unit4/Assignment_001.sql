CREATE DATABASE animalshp;

\c animalshp

CREATE TABLE animals(
  species varchar(20) primary key,
  vertebrate_class varchar(20) NOT NULL,
  appearance varchar(20) NOT NULL,
  num_leg int NOT NULL
);

CREATE TABLE pets(
  name varchar(20) primary key,
  species varchar(20) NOT NULL,
  owner varchar(100) NOT NULL,
  gender varchar(20) NOT NULL,
  color varchar(20) NOT NULL
);

INSERT INTO animals VALUES ('cat','mammal','fur',4);
INSERT INTO animals VALUES ('rat','mammal','fur',4);
INSERT INTO animals VALUES ('owl','bird','feathers',2);
INSERT INTO animals VALUES ('snake','reptile','dryscales',0);
INSERT INTO animals VALUES ('toad','amphibian','smoothskin',4);
INSERT INTO animals VALUES ('alligator','reptile','dry scales',4);

INSERT INTO pets VALUES ('Nagini','snake','Lord Voldemort','female','green');
INSERT INTO pets VALUES ('Hedwig','owl','Harry Potter','female','snow white');
INSERT INTO pets VALUES ('Scabbers','rat','Ron Weasley','male','unspecified');
INSERT INTO pets VALUES ('Pigwidgeon','owl','Ron Weasley','male','grey');
INSERT INTO pets VALUES ('Crookshanks','cat','Herminone Granger','male','ginger');
INSERT INTO pets VALUES ('Mrs Norris','cat','Argus Filch','female','dust-coloured');
INSERT INTO pets VALUES ('Trevor','toad','Neville Longbottom','male','brown');

SELECT * FROM pets;
SELECT * FROM animals;

select appearance from animals where species='rat';
select species from animals where vertebrate_class in ('mammal','amphibian');
select species from animals where num_legs between 1 and 3;
select species from animals where appearance like '%f%';
select p.name, case when length(p.name) > 6 then 'long' else 'short' end from pets p where p.gender = 'female';

select distinct a.species from animals a join pets p on p.species = a.species;
select count(*) from pets p where p.owner = 'Ron Weasley';
select 'Ron Weasley has '||count(*)||' pets' from pets p where p.owner = 'Ron Weasley';
select p.owner||' has '||count(*)||' pets' from pets p group by owner;
select p.owner from pets p group by owner having count(*)=1;

select p.name, a.vertebrate_class from pets p join animals a on a.species = p.species;
select p.name, a.appearance,p.color from pets p join animals a on a.species = p.species;
select p.name, a.vertebrate_class from pets p join animals a on a.species = p.species where p.gender='male';
select p.owner from pets p join animals a on a.species = p.species group by p.owner having count(distinct a.vertebrate_class)>1;
select p.owner from pets p group by owner having count(*)=1;

select count(*) from beds where facility_id='6057'

select cast(bed_census_date as date) as bed_census_date_date from beds
where facility_id='6057'
order by bed_census_date_date limit 1;

select cast(bed_census_date as date) as bed_census_date_date from beds
where facility_id='6057'
order by bed_census_date_date desc limit 1;

select facility_id, facility_name, available_residential_beds from beds
order by cast(available_residential_beds as int) desc,facility_id
limit 10;

1. get the greatest number for each facility_id
2. top 10

select * from
(select facility_id, facility_name, max(cast(available_residential_beds as int)) as num from beds
group by facility_id, facility_name) sub
order by sub.num desc
limit 10;
