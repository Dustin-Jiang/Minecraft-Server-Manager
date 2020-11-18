execute @a[score_dead_min=1] ~ ~ ~ function bic:dead
scoreboard players set @s teams 0
execute @a[team=blue,c=1,m=!3] ~ ~ ~ scoreboard players add @e[name=map] teams 1
execute @a[team=red,c=1,m=!3] ~ ~ ~ scoreboard players add @e[name=map] teams 1
execute @a[team=yellow,c=1,m=!3] ~ ~ ~ scoreboard players add @e[name=map] teams 1
execute @a[team=green,c=1,m=!3] ~ ~ ~ scoreboard players add @e[name=map] teams 1
execute @a[m=!3] ~ ~ ~ fill ~-1 ~-1 ~-1 ~1 ~1 ~1 air 0 replace portal
function bic:smelt if @s[tag=smelt]
scoreboard players tag @e[type=item] add sapling {Item:{id:"minecraft:sapling"}}
entitydata @e[tag=sapling] {Tags:[],Item:{id:"apple"}}
function bic:end if @s[score_teams=1]
function bic:weakness if @s[score_weakness_min=1]
function bic:glowing if @s[score_glowing_min=1]
gamemode 3 @a[x=32,y=1,z=32,dx=63,dy=15,dz=63]
execute @a[m=3] ~ ~ ~ tp @s[y=-64,dy=-64] ~ 5 ~
tp @a[x=32,y=1,z=32,dx=63,dy=15,dz=63] 1040.0 10 1040.0