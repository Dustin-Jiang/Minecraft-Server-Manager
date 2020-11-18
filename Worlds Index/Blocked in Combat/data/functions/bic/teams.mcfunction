execute @a[team=!blue] ~ ~ ~ detect ~ ~-1 ~ wool 11 scoreboard teams leave @s
execute @a[team=!blue] ~ ~ ~ detect ~ ~-1 ~ wool 11 tellraw @a [{"selector":"@s","color":"gray"},{"text":" joined team blue","color":"blue"}]
execute @a[team=!blue] ~ ~ ~ detect ~ ~-1 ~ wool 11 scoreboard teams join blue @s
execute @a[team=!red] ~ ~ ~ detect ~ ~-1 ~ wool 14 scoreboard teams leave @s
execute @a[team=!red] ~ ~ ~ detect ~ ~-1 ~ wool 14 tellraw @a [{"selector":"@s","color":"gray"},{"text":" joined team red","color":"red"}]
execute @a[team=!red] ~ ~ ~ detect ~ ~-1 ~ wool 14 scoreboard teams join red @s
execute @a[team=!yellow] ~ ~ ~ detect ~ ~-1 ~ wool 4 scoreboard teams leave @s
execute @a[team=!yellow] ~ ~ ~ detect ~ ~-1 ~ wool 4 tellraw @a [{"selector":"@s","color":"gray"},{"text":" joined team yellow","color":"yellow"}]
execute @a[team=!yellow] ~ ~ ~ detect ~ ~-1 ~ wool 4 scoreboard teams join yellow @s
execute @a[team=!green] ~ ~ ~ detect ~ ~-1 ~ wool 5 scoreboard teams leave @s
execute @a[team=!green] ~ ~ ~ detect ~ ~-1 ~ wool 5 tellraw @a [{"selector":"@s","color":"gray"},{"text":" joined team green","color":"green"}]
execute @a[team=!green] ~ ~ ~ detect ~ ~-1 ~ wool 5 scoreboard teams join green @s
execute @a[team=!spectator] ~ ~ ~ detect ~ ~-1 ~ wool 8 scoreboard teams leave @s
execute @a[team=!spectator] ~ ~ ~ detect ~ ~-1 ~ wool 8 tellraw @a [{"selector":"@s","color":"gray"},{"text":" will be a spectator","color":"gray"}]
execute @a[team=!spectator] ~ ~ ~ detect ~ ~-1 ~ wool 8 scoreboard teams join spectator @s
tp @a[x=32,y=1,z=32,dx=31,dy=15,dz=63] 76 5 47