create table Members(
  id integer not null PRIMARY KEY,
  name varchar(256),
  email varchar(64) UNIQUE);
  
create table Students(
  goals varchar(1000),
  student_id integer PRIMARY KEY,
  foreign key (student_id) references Members(id));
  
create table Teachers(
  bio varchar(1000),
  teacher_id integer PRIMARY KEY,
  foreign key (teacher_id) references Members(id));
  
create table Trackables(
  id integer,
  name varchar(48),
  instrument varchar(48),
  primary key(name, instrument));
  
create table Recordings(
  id integer,
  day date,
  trackable_name varchar(48),
  trackable_instrument varchar(48),
  duration integer,
  location varchar(100) ,
  student integer references Students(student_id),
  primary key(day, student, trackable_name, trackable_instrument),
  foreign key (trackable_name, trackable_instrument) references Trackables(name,instrument));
  
create table Notes(
  id integer,
  student_id integer references Students(student_id),
  trackable_name varchar(48),
  trackable_instrument varchar(48),
  note varchar(1000),
  primary key (student_id, trackable_name, trackable_instrument),
  foreign key (trackable_name, trackable_instrument) references Trackables(name,instrument));
  
create table IsStudentOf(
  id integer,
  student_id integer references Students(student_id),
  teacher_id integer references Teachers(teacher_id),
  instrument varchar(48),
  start_date date,
  end_date date,
  primary key(student_id, teacher_id, start_date, instrument));
  
create table Creates(
  id integer,
  trackable_name varchar(48),
  trackable_instrument varchar(48),
  teacher_id integer references Teachers(teacher_id),
  student_id integer references Students(student_id),
  date_assigned date,
  date_removed date,
  active integer CHECK(active IN (0,1)),
  current_duration integer,
  primary key(trackable_name, trackable_instrument, teacher_id, student_id, date_assigned), 
  foreign key (trackable_name, trackable_instrument) references Trackables(name, instrument));
 
create table IsAssigned(
  id integer,
  practice_day date,
  time integer,
  student_id integer references Students(student_id),
  trackable_name varchar(48),
  trackable_instrument varchar(48),
  primary key(practice_day, student_id, trackable_name, trackable_instrument),
  foreign key (trackable_name, trackable_instrument) references Trackables(name, instrument));
