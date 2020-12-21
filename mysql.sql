--分配权限
grant select,update on c_j.cls to 'changjuan'@'%' identified by '123' with grant option;

--删除权限
revoke delete on c_j.cls from 'changjuan'@'%';
