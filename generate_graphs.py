import matplotlib.pyplot as plt

models = ['ResNet-18', 'MobileNet-V2']
energy = [7.9885, 4.3337]
latency = [443.41, 215.9]

plt.figure(figsize=(8, 5))
bars = plt.bar(models, energy, color=['#ff6b6b', '#1dd1a1'])
plt.ylabel('Energy Consumption (Joules)')
plt.title('EcoCompute: Energy Comparison Between AI Models')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f"{yval} J", ha='center', va='bottom')

plt.tight_layout()
plt.savefig('energy_comparison.png')
print("Graph saved successfully as energy_comparison.png")