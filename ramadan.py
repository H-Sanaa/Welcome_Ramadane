from turtle import*


bgcolor('black')
penup()
goto(0,-60)
pendown()#abaisse la tortue pour recommencer a dessiner

color('white')
begin_fill()
circle(60)
end_fill()

penup()
goto(18,-54)
pendown()#abaisse la tortue pour recommencer a dessiner
color('black')
begin_fill()
circle(54)

end_fill()
color('white')
begin_fill()
style=('Couier',30,'bold')
write('رمضان كريم',font=style,align='left')
end_fill()
penup()
goto(50,50)
pendown()
color('yellow')
begin_fill()

for i in range(5):
   forward(10)
   left(144)

end_fill()
penup()
goto(100,30)# pour fait le posissenement goto(x,y)
pendown()
color('yellow')
begin_fill()
for i in range(5):
   forward(20)
   left(144)
end_fill()

penup()
goto(-100,-40)# pour fait le posissenement goto(x,y)
pendown()
color('yellow')
begin_fill()
for i in range(5):
   forward(20)
   left(144)
end_fill()

penup()
goto(-130,5)# pour fait le posissenement goto(x,y)
pendown()
color('yellow')
begin_fill()
for i in range(5):
   forward(10)
   left(150)
end_fill()


done()







