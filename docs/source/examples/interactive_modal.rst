Analyse modale interactive
==========================

Cette démonstration permet de modifier le diamètre,
le module d'Young et la longueur de la poutre.

.. thebe-button::

.. code-block:: python
   :class: thebe

  
    import numpy as np
    import matplotlib.pyplot as plt
    import ipywidgets as widgets

    from IPython.display import display, clear_output
    from beamsolve import beam as beam_module
    from beamsolve import FEM


    # --------------------------------------------------
    # 1. Fonction de calcul FEM
    # --------------------------------------------------

    def calculate_modes(d, E, L):

        A, I = beam_module.circular_section(d=d)

        current_beam = beam_module.Beam(
            L=L,
            E=E,
            rho=7800,
            A=A,
            I=I,
            bc_left="pinned",
            bc_right="pinned"
        )

        fem_model = FEM.FEMModel(
            beam=current_beam,
            ne=20
        )

        sol_fem = fem_model.solve_modes(n_modes=4)

        return sol_fem


    # --------------------------------------------------
    # 2. Fonction de mise à jour
    # --------------------------------------------------

    def update(d, E, L):

        with output:

            clear_output(wait=True)
            plt.close("all")

            # Calcul FEM
            sol_fem = calculate_modes(d, E, L)

            # Affichage des paramètres
            print("PARAMÈTRES DE LA POUTRE")
            print(f"Diamètre : {d*1000:.1f} mm")
            print(f"Module d'Young : {E/1e9:.1f} GPa")
            print(f"Longueur : {L:.2f} m")

            # Affichage des fréquences
            print("\nFRÉQUENCES PROPRES FEM")

            for k, f in enumerate(sol_fem.frequencies):
                print(f"Mode {k+1}: {f:.3f} Hz")

            # Visualisation des formes modales
            FEM.visualisation.plot_mode_shapes(sol_fem)


    # --------------------------------------------------
    # 3. Définition des curseurs
    # --------------------------------------------------

    diameter = widgets.FloatSlider(
        value=0.010,
        min=0.005,
        max=0.020,
        step=0.001,
        description="Diamètre (m)",
        continuous_update=False
    )

    young_modulus = widgets.FloatSlider(
        value=70e9,
        min=10e9,
        max=210e9,
        step=10e9,
        description="E (Pa)",
        continuous_update=False
    )

    length = widgets.FloatSlider(
        value=0.50,
        min=0.20,
        max=1.00,
        step=0.05,
        description="Longueur (m)",
        continuous_update=False
    )


    # --------------------------------------------------
    # 4. Interface interactive
    # --------------------------------------------------

    controls = widgets.VBox([
        diameter,
        young_modulus,
        length
    ])

    output = widgets.interactive_output(
        update,
        {
            "d": diameter,
            "E": young_modulus,
            "L": length
        }
    )

    display(controls, output)
