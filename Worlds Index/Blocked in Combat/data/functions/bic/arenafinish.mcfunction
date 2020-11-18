fill 1025 11 1025 1054 11 1054 bedrock
effect @a clear
gamemode 3 @a[team=spectator]
gamemode 0 @a[m=!3]
spreadplayers 1040.0 1040.0 12 13 true @a[m=!3]
tp @a[m=!3] ~ 5 ~
execute @a[m=!3] ~ ~ ~ fill ~ ~ ~ ~1 ~1 ~1 air
execute @a[m=!3] ~ ~ ~ setblock ~ ~-1 ~ air
execute @s[tag=chest] ~ ~ ~ execute @a[m=!3] ~ ~ ~ setblock ~ ~-1 ~ chest 0 keep {LootTable:"chests/spawn_bonus_chest"}
title @a title {"text":"GO!","color":"aqua"}
title @a subtitle [""]
execute @a ~ ~ ~ playsound entity.player.levelup master @s
scoreboard players operation @s weakness = @s nopvp
scoreboard players operation @s weakness *= #1200 display
scoreboard players operation @s glowing = @s glow
scoreboard players operation @s glowing *= #1200 display
scoreboard players tag @s add play