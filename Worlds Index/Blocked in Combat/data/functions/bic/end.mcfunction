title @a times 0 100 50
execute @a[team=blue,c=1,m=!3] ~ ~ ~ title @a title {"text":"Blue wins!","color":"blue"}
execute @a[team=red,c=1,m=!3] ~ ~ ~ title @a title {"text":"Red wins!","color":"red"}
execute @a[team=yellow,c=1,m=!3] ~ ~ ~ title @a title {"text":"Yellow wins!","color":"yellow"}
execute @a[team=green,c=1,m=!3] ~ ~ ~ title @a title {"text":"Green wins!","color":"green"}
gamemode 2 @a
tp @a 49 8 80 0 0
clear @a
effect @a clear
xp -999L @a
tellraw @a {"text":"\nThe game has ended!","color":"aqua"}
effect @a clear
scoreboard players tag @s remove play
scoreboard players reset Combat display
scoreboard players reset Glowing display