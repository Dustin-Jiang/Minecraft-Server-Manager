scoreboard players tag @e[tag=on] remove on
execute @e[tag=block] ~ ~ ~ detect ~ ~1 ~1 lit_redstone_lamp 0 scoreboard players tag @s add on
execute @e[tag=block] ~ ~ ~ detect ~ ~-1 ~1 lit_redstone_lamp 0 scoreboard players tag @s add on
scoreboard players tag @s remove lamp
execute @e[c=1,tag=on] ~ ~ ~ scoreboard players tag @e[name=map] add lamp
scoreboard players set @s teams 0
execute @e[tag=block] ~ ~ ~ scoreboard players tag @e[tag=block] add lamp
execute @a[team=blue,c=1] ~ ~ ~ scoreboard players add @e[name=map] teams 1
execute @a[team=red,c=1] ~ ~ ~ scoreboard players add @e[name=map] teams 1
execute @a[team=yellow,c=1] ~ ~ ~ scoreboard players add @e[name=map] teams 1
execute @a[team=green,c=1] ~ ~ ~ scoreboard players add @e[name=map] teams 1
scoreboard players set @s[score_teams_min=2,tag=lamp] countdown 0
execute @s[tag=!lamp,score_teams_min=1] ~ ~ ~ tellraw @a {"text":"At least one block needs to be enabled to start the game!","color":"aqua"}
execute @s[score_teams=1] ~ ~ ~ tellraw @a {"text":"You need a player on at least two teams to start the game!","color":"aqua"}