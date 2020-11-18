execute @e[name=arena] ~ ~ ~ function bic:arena if @e[name=map,score_countdown_min=2]
execute @e[name=arena] ~ ~ ~ tp @s ~-30 ~ ~1
execute @e[name=arena] ~ ~ ~ detect ~ ~ ~ bedrock 0 tp @s ~ ~1 ~-30
tp @a 1040.0 30 1040.0 0 90
function bic:cancel if @a[score_stop_min=1]
execute @s[score_countdown=1] ~ ~ ~ tp @e[name=arena] 1025 1 1025
execute @s[score_countdown=1] ~ ~ ~ fill 1025 1 1025 1054 11 1054 air
execute @s[score_countdown_min=102] ~ ~ ~ title @a title {"text":"Starting in...","color":"aqua"}
execute @s[score_countdown_min=102,score_countdown=102] ~ ~ ~ title @a times 0 40 20
execute @s[score_countdown_min=102,score_countdown=102] ~ ~ ~ title @a subtitle ["10"]
execute @s[score_countdown_min=102,score_countdown=102] ~ ~ ~ execute @a ~ ~ ~ playsound entity.experience_orb.pickup master @s
execute @s[score_countdown_min=122,score_countdown=122] ~ ~ ~ title @a subtitle ["9"]
execute @s[score_countdown_min=122,score_countdown=122] ~ ~ ~ execute @a ~ ~ ~ playsound entity.experience_orb.pickup master @s
execute @s[score_countdown_min=142,score_countdown=142] ~ ~ ~ title @a subtitle ["8"]
execute @s[score_countdown_min=142,score_countdown=142] ~ ~ ~ execute @a ~ ~ ~ playsound entity.experience_orb.pickup master @s
execute @s[score_countdown_min=162,score_countdown=162] ~ ~ ~ title @a subtitle ["7"]
execute @s[score_countdown_min=162,score_countdown=162] ~ ~ ~ execute @a ~ ~ ~ playsound entity.experience_orb.pickup master @s
execute @s[score_countdown_min=182,score_countdown=182] ~ ~ ~ title @a subtitle ["6"]
execute @s[score_countdown_min=182,score_countdown=182] ~ ~ ~ execute @a ~ ~ ~ playsound entity.experience_orb.pickup master @s
execute @s[score_countdown_min=202,score_countdown=202] ~ ~ ~ title @a subtitle ["5"]
execute @s[score_countdown_min=202,score_countdown=202] ~ ~ ~ execute @a ~ ~ ~ playsound entity.experience_orb.pickup master @s
execute @s[score_countdown_min=222,score_countdown=222] ~ ~ ~ title @a subtitle ["4"]
execute @s[score_countdown_min=222,score_countdown=222] ~ ~ ~ execute @a ~ ~ ~ playsound entity.experience_orb.pickup master @s
execute @s[score_countdown_min=242,score_countdown=242] ~ ~ ~ title @a subtitle ["3"]
execute @s[score_countdown_min=242,score_countdown=242] ~ ~ ~ execute @a ~ ~ ~ playsound entity.experience_orb.pickup master @s
execute @s[score_countdown_min=262,score_countdown=262] ~ ~ ~ title @a subtitle ["2"]
execute @s[score_countdown_min=262,score_countdown=262] ~ ~ ~ execute @a ~ ~ ~ playsound entity.experience_orb.pickup master @s
execute @s[score_countdown_min=282,score_countdown=282] ~ ~ ~ title @a subtitle ["1"]
execute @s[score_countdown_min=282,score_countdown=282] ~ ~ ~ execute @a ~ ~ ~ playsound entity.experience_orb.pickup master @s
function bic:arenafinish if @s[score_countdown_min=302,score_countdown=302]
scoreboard players add @s countdown 1