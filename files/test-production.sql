select AVG(time) 
from IsAssigned x, IsStudentOf y 
where x.student_id = y.student_id and teacher_id = 2 
group by teacher_id; 

select avg(duration) 
from Recordings;

select sum(duration)/count(distinct day) as avg 
from Recordings 
where student = 1;

select count(*) 
from IsStudentOf 
where teacher_id = 2;

select sum(duration) 
from Recordings 
where student = 1 and day = DATE '2019-01-06';

select sum(time) 
from IsAssigned 
where practice_day = DATE '2019-01-05' 
AND student_id = 1;

select sum(duration) 
from Recordings 
where student = 1 and day = DATE '2019-01-02' and trackable_instrument = 'Piano';

select time, trackable_name 
from (select practice_day, time, student_id, trackable_name,instrument 
	from IsAssigned 
	join Trackables on IsAssigned.trackable_name = Trackables.name) as sub 
where student_id = 1 and instrument = 'Piano' and practice_day = DATE '2019-01-03';

select sum(time) / count(distinct practice_day) 
from IsAssigned 
where student_id = 1 and trackable_instrument = 'Piano';