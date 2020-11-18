effect @a night_vision 16 0 true
execute @e[name=map,tag=!play] ~ ~ ~ effect @a saturation 16 0 true
execute @e[name=map,tag=!play] ~ ~ ~ effect @a weakness 1 255 true
execute @a ~ ~ ~ detect ~ ~ ~ bed -1 tp @s 49 8 80 0 0
execute @a[x=1008,y=-16,z=1008,dx=63,dy=63,dz=63] ~ ~ ~ function bic:join if @e[name=map,tag=!play,score_countdown_min=303]
execute @a[tag=!join] ~ ~ ~ function bic:join
execute @e[name=map] ~ ~ ~ function bic:main
scoreboard objectives add display dummy §b§lBlocked in Combat§r