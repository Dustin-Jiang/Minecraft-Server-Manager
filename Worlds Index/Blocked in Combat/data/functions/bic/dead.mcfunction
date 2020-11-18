spawnpoint @s
gamemode 3 @s
tellraw @a [{"selector":"@s"},{"text":" is now a spectator!","color":"gray"}]
scoreboard players set @s dead 0