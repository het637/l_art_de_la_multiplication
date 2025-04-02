import turtle as t


t.setup(800, 600)
t.speed(0)
t.penup()
t.goto(0, -200)
t.pendown()
t.circle(200)
t.penup()

nbr_pts = int(input("Combien de points sur le cercle ? "))
table = int(input("Quelle table de multiplication ? "))


esp_pts = 360 / nbr_pts
coord_points = []

for _ in range(nbr_pts):
    t.dot(5, "red")
    coord_points.append(t.position())
    t.circle(200, esp_pts)

for i in range(nbr_pts):
    depart = i
    arrivee = (i * table) % nbr_pts
    t.penup()
    t.goto(coord_points[depart])
    t.pendown()
    t.goto(coord_points[arrivee])

t.exitonclick()
