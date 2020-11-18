execute @e[name=lever] ~ ~ ~ detect ~ ~ ~ lever 11 blockdata ~ ~ ~-2 {auto:1}
execute @e[name=lever] ~ ~ ~ detect ~ ~ ~ lever 11 blockdata ~ ~1 ~-2 {auto:0}
execute @e[name=lever] ~ ~ ~ detect ~ ~ ~ lever 3 blockdata ~ ~ ~-2 {auto:0}
execute @e[name=lever] ~ ~ ~ detect ~ ~ ~ lever 3 blockdata ~ ~1 ~-2 {auto:1}
execute @e[tag=warn] ~ ~ ~ detect ~ ~1 ~-1 lever 4 blockdata ~ ~1 ~2 {auto:1}
execute @e[tag=warn] ~ ~ ~ detect ~ ~1 ~-1 lever 12 blockdata ~ ~1 ~2 {auto:0}
replaceitem block 89 3 88 slot.container.0 egg 1 0 {display:{LocName:"Easter Egg II"}}
clear @a egg