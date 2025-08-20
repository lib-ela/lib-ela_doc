# Generate three figures for the "Motivations" page and save them to /mnt/data
import numpy as np
import matplotlib.pyplot as plt

# 1) Uniaxial Cauchy stress for incompressible Neo-Hookean: sigma = mu * (lambda^2 - 1/lambda)
lmbda = np.linspace(0.6, 2.0, 400)
mus = [50e3, 100e3, 200e3]  # Pa
plt.figure()
for mu in mus:
    sigma = mu * (lmbda**2 - 1.0/lmbda)
    plt.plot(lmbda, sigma, label=f"μ = {mu/1000:.0f} kPa")
plt.xlabel("Stretch λ")
plt.ylabel("Cauchy stress σ (Pa)")
plt.title("Uniaxial Neo-Hookean Response (Incompressible)")
plt.legend()
plt.grid(True, linewidth=0.3)
plt.tight_layout()
uniaxial_path = "/mnt/data/motivations_uniaxial.png"
plt.savefig(uniaxial_path, dpi=160)
plt.close()

# 2) Simple shear: τ = μ γ for incompressible Neo-Hookean
gamma = np.linspace(0.0, 2.0, 300)
plt.figure()
for mu in mus:
    tau = mu * gamma
    plt.plot(gamma, tau, label=f"μ = {mu/1000:.0f} kPa")
plt.xlabel("Shear strain γ")
plt.ylabel("Shear stress τ (Pa)")
plt.title("Simple Shear (Neo-Hookean, Incompressible)")
plt.legend()
plt.grid(True, linewidth=0.3)
plt.tight_layout()
shear_path = "/mnt/data/motivations_shear.png"
plt.savefig(shear_path, dpi=160)
plt.close()

# 3) 3D Energy surface: W(λ1, λ2) for incompressible Neo-Hookean
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

lam1 = np.linspace(0.6, 1.8, 120)
lam2 = np.linspace(0.6, 1.8, 120)
L1, L2 = np.meshgrid(lam1, lam2)
L3 = 1.0 / (L1 * L2)  # incompressibility: det F = 1
mu = 100e3  # Pa
I1 = L1**2 + L2**2 + L3**2
W = 0.5 * mu * (I1 - 3.0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(L1, L2, W, linewidth=0, antialiased=True)
ax.set_xlabel("λ₁")
ax.set_ylabel("λ₂")
ax.set_zlabel("Energy W (J/m³)")
ax.set_title("Neo-Hookean Energy Surface (Incompressible, μ=100 kPa)")
plt.tight_layout()
energy_surface_path = "/mnt/data/motivations_energy_surface.png"
plt.savefig(energy_surface_path, dpi=160)
plt.close()

uniaxial_path, shear_path, energy_surface_path
