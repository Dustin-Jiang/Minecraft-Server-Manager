scoreboard players remove @s glowing 1
scoreboard players operation @s dead = @s glowing
scoreboard players operation @s dead %= #20 display
execute @s[score_dead=0] ~ ~ ~ scoreboard players operation Glowing display = @s glowing
execute @s[score_dead=0] ~ ~ ~ scoreboard players operation Glowing display /= #20 display
function bic:glowcount if @s[score_glowing=100,score_glowing_min=20,score_dead=0]
function bic:glowgive if @s[score_glowing=0]