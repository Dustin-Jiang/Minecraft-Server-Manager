tp @a 49 8 80 0 0
scoreboard players set @s countdown 303
tellraw @a {"text":"\nThe game has been cancelled!","color":"aqua"}
effect @a clear
scoreboard players reset @a[score_stop_min=1] stop