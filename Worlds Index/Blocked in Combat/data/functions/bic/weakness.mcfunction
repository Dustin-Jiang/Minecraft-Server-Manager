scoreboard players remove @s weakness 1
scoreboard players operation @s dead = @s weakness
scoreboard players operation @s dead %= #20 display
execute @s[score_dead=0] ~ ~ ~ scoreboard players operation Combat display = @s weakness
execute @s[score_dead=0] ~ ~ ~ scoreboard players operation Combat display /= #20 display
function bic:combatcount if @s[score_weakness=100,score_weakness_min=20,score_dead=0]
function bic:combatgive if @s[score_weakness=0]
execute @s[score_weakness_min=20] ~ ~ ~ effect @a[m=!3] weakness 1 255 true