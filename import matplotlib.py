import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))
ax.axis('off')

# Define component positions and sizes
components = {
    'Clients\n(Web/Mobile)': (0.1, 0.8),
    'API Gateway': (0.35, 0.8),
    'Auth Service': (0.1, 0.55),
    'User Service': (0.35, 0.55),
    'Order Service': (0.6, 0.55),
    'Database\n(SQL/NoSQL)': (0.35, 0.25),
    'Cache': (0.6, 0.25),
    'Message Queue': (0.1, 0.25),
}

width = 0.2
height = 0.1

# Draw components
for label, (x, y) in components.items():
    rect = Rectangle((x, y), width, height, fill=False, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x + width/2, y + height/2, label, ha='center', va='center')

# Function to draw arrows between components
def draw_arrow(start_label, end_label):
    sx, sy = components[start_label]
    ex, ey = components[end_label]
    start = (sx + width, sy + height/2)
    end = (ex, ey + height/2)
    arrow = Line2D([start[0], end[0]], [start[1], end[1]], 
                   linewidth=1.2, marker='>', color='black')
    ax.add_line(arrow)

# Draw arrows representing interactions
draw_arrow('Clients\n(Web/Mobile)', 'API Gateway')
draw_arrow('API Gateway', 'Auth Service')
draw_arrow('API Gateway', 'User Service')
draw_arrow('API Gateway', 'Order Service')
draw_arrow('Auth Service', 'Database\n(SQL/NoSQL)')
draw_arrow('User Service', 'Database\n(SQL/NoSQL)')
draw_arrow('Order Service', 'Message Queue')
draw_arrow('Order Service', 'Cache')
draw_arrow('Message Queue', 'Database\n(SQL/NoSQL)')

# Display the diagram
plt.show()
