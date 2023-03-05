use iair;
select database();

# create a new user iair, with full functionality. This is to prevent leakage host password when going opensource with flask.
create user 'iair'@'localhost' identified by 'iair';
grant all privileges on iair.* to 'iair'@'localhost';
