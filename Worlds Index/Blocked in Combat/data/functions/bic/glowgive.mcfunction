tellraw @a {"text":"Players are glowing now!","color":"aqua"}
execute @a ~ ~ ~ playsound entity.evocation_illager.prepare_summon master @s
effect @a[m=!3] glowing 999999 0 true
scoreboard players reset Glowing display