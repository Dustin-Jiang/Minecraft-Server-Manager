tp @a 1040.0 30 1040.0 0 90
effect @a levitation 16 255 true
effect @a weakness 16 255 true
effect @a invisibility 16 0 true
tellraw @a [{"text":"\nThe game has been started. Click here to cancel the game.","color":"aqua","clickEvent":{"action":"run_command","value":"/trigger stop set 1"}}]
scoreboard players enable @a stop
scoreboard players add @s countdown 1
replaceitem entity @a slot.enderchest.0 air
replaceitem entity @a slot.enderchest.1 air
replaceitem entity @a slot.enderchest.2 air
replaceitem entity @a slot.enderchest.3 air
replaceitem entity @a slot.enderchest.4 air
replaceitem entity @a slot.enderchest.5 air
replaceitem entity @a slot.enderchest.6 air
replaceitem entity @a slot.enderchest.7 air
replaceitem entity @a slot.enderchest.8 air
replaceitem entity @a slot.enderchest.9 air
replaceitem entity @a slot.enderchest.10 air
replaceitem entity @a slot.enderchest.11 air
replaceitem entity @a slot.enderchest.12 air
replaceitem entity @a slot.enderchest.13 air
replaceitem entity @a slot.enderchest.14 air
replaceitem entity @a slot.enderchest.15 air
replaceitem entity @a slot.enderchest.16 air
replaceitem entity @a slot.enderchest.17 air
replaceitem entity @a slot.enderchest.18 air
replaceitem entity @a slot.enderchest.19 air
replaceitem entity @a slot.enderchest.20 air
replaceitem entity @a slot.enderchest.21 air
replaceitem entity @a slot.enderchest.22 air
replaceitem entity @a slot.enderchest.23 air
replaceitem entity @a slot.enderchest.24 air
replaceitem entity @a slot.enderchest.25 air
replaceitem entity @a slot.enderchest.26 air