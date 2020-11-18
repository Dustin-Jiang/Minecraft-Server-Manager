scoreboard players tag @e[type=item] add iron {Item:{id:"minecraft:iron_ore"}}
scoreboard players tag @e[type=item] add gold {Item:{id:"minecraft:gold_ore"}}
execute @e[tag=iron] ~ ~ ~ summon xp_orb ~ ~ ~ {Value:1}
execute @e[tag=gold] ~ ~ ~ summon xp_orb ~ ~ ~ {Value:1}
entitydata @e[tag=iron] {Tags:[],Item:{id:"iron_ingot"}}
entitydata @e[tag=gold] {Tags:[],Item:{id:"gold_ingot"}}