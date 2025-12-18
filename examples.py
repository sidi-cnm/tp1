"""
Script d'exemples pour la bibliothèque VizStyle
==============================================

Ce script démontre l'utilisation de toutes les fonctions de visualisation
disponibles dans VizStyle.

"""

import numpy as np
import vizstyle

def example_1_styled_line():
    """Exemple 1: Graphique en ligne simple et multiple"""
    print("=" * 60)
    print("Exemple 1: Graphiques en ligne")
    print("=" * 60)
    
    # Une seule courbe
    x = np.linspace(0, 10, 50)
    y = np.sin(x)
    
    print("\n1.1 - Courbe simple (fonction sinus)")
    vizstyle.styled_line(
        x=x,
        y=y,
        title="Fonction Sinus",
        xlabel="x",
        ylabel="sin(x)"
    )
    
    # Plusieurs courbes
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) * np.exp(-x/10)
    
    print("\n1.2 - Courbes multiples")
    vizstyle.styled_line(
        x=x,
        y=[y1, y2, y3],
        title="Fonctions trigonométriques",
        xlabel="x",
        ylabel="y",
        label=['sin(x)', 'cos(x)', 'sin(x)·exp(-x/10)']
    )


def example_2_styled_scatter():
    """Exemple 2: Nuages de points"""
    print("\n" + "=" * 60)
    print("Exemple 2: Nuages de points")
    print("=" * 60)
    
    # Corrélation linéaire
    np.random.seed(42)
    x = np.random.randn(100)
    y = 2 * x + np.random.randn(100) * 0.5
    
    print("\n2.1 - Corrélation linéaire")
    vizstyle.styled_scatter(
        x=x,
        y=y,
        title="Corrélation linéaire (r ≈ 0.97)",
        xlabel="Variable X",
        ylabel="Variable Y",
        color='#A23B72',
        size=100
    )
    
    # Points avec tailles variables
    x2 = np.random.rand(50) * 10
    y2 = np.random.rand(50) * 10
    sizes = np.random.rand(50) * 300 + 50
    
    print("\n2.2 - Points avec tailles variables")
    vizstyle.styled_scatter(
        x=x2,
        y=y2,
        title="Scatter plot avec tailles variables",
        xlabel="X",
        ylabel="Y",
        size=sizes,
        color='#F18F01'
    )


def example_3_styled_bar():
    """Exemple 3: Graphiques en barres"""
    print("\n" + "=" * 60)
    print("Exemple 3: Graphiques en barres")
    print("=" * 60)
    
    # Barres simples verticales
    categories = ['Produit A', 'Produit B', 'Produit C', 'Produit D', 'Produit E']
    values = [234, 456, 389, 512, 298]
    
    print("\n3.1 - Barres verticales simples")
    vizstyle.styled_bar(
        x=categories,
        y=values,
        title="Ventes par produit",
        xlabel="Produits",
        ylabel="Ventes (unités)",
        color='#06A77D'
    )
    
    # Barres horizontales
    print("\n3.2 - Barres horizontales")
    vizstyle.styled_bar(
        x=categories,
        y=values,
        title="Classement des produits",
        xlabel="Ventes (unités)",
        ylabel="Produits",
        horizontal=True,
        color='#2E86AB'
    )
    
    # Barres groupées
    q1 = [234, 456, 389, 512, 298]
    q2 = [256, 478, 412, 495, 321]
    q3 = [289, 501, 445, 534, 356]
    
    print("\n3.3 - Barres groupées (comparaison trimestrielle)")
    vizstyle.styled_bar(
        x=categories,
        y=[q1, q2, q3],
        title="Ventes par trimestre",
        xlabel="Produits",
        ylabel="Ventes (unités)",
        labels=['Q1 2024', 'Q2 2024', 'Q3 2024']
    )


def example_4_styled_histogram():
    """Exemple 4: Histogrammes"""
    print("\n" + "=" * 60)
    print("Exemple 4: Histogrammes")
    print("=" * 60)
    
    # Distribution normale
    np.random.seed(42)
    data_normal = np.random.normal(loc=100, scale=15, size=1000)
    
    print("\n4.1 - Distribution normale")
    vizstyle.styled_histogram(
        data=data_normal,
        bins=30,
        title="Distribution des scores (μ=100, σ=15)",
        xlabel="Score",
        ylabel="Densité",
        kde=True,
        color='#2E86AB'
    )
    
    # Distribution bimodale
    data_bimodal = np.concatenate([
        np.random.normal(60, 8, 500),
        np.random.normal(120, 10, 500)
    ])
    
    print("\n4.2 - Distribution bimodale")
    vizstyle.styled_histogram(
        data=data_bimodal,
        bins=40,
        title="Distribution bimodale",
        xlabel="Valeur",
        ylabel="Densité",
        kde=True,
        color='#F18F01'
    )
    
    # Distribution asymétrique
    data_skewed = np.random.gamma(2, 2, 1000)
    
    print("\n4.3 - Distribution asymétrique (Gamma)")
    vizstyle.styled_histogram(
        data=data_skewed,
        bins=35,
        title="Distribution asymétrique (loi Gamma)",
        xlabel="Valeur",
        ylabel="Densité",
        kde=True,
        color='#06A77D'
    )


def example_5_styled_heatmap():
    """Exemple 5: Cartes de chaleur"""
    print("\n" + "=" * 60)
    print("Exemple 5: Cartes de chaleur")
    print("=" * 60)
    
    # Matrice de corrélation
    np.random.seed(42)
    n_vars = 8
    data = np.random.randn(100, n_vars)
    # Ajouter des corrélations
    data[:, 1] = data[:, 0] * 0.8 + np.random.randn(100) * 0.2
    data[:, 3] = data[:, 2] * 0.6 + np.random.randn(100) * 0.4
    
    corr_matrix = np.corrcoef(data.T)
    labels = [f'Var{i+1}' for i in range(n_vars)]
    
    print("\n5.1 - Matrice de corrélation")
    vizstyle.styled_heatmap(
        data=corr_matrix,
        title="Matrice de corrélation entre variables",
        xticklabels=labels,
        yticklabels=labels,
        cmap='RdBu_r',
        annot=True,
        fmt='.2f'
    )
    
    # Matrice de confusion
    confusion_matrix = np.array([
        [92, 5, 3],
        [4, 88, 8],
        [2, 6, 92]
    ])
    classes = ['Classe A', 'Classe B', 'Classe C']
    
    print("\n5.2 - Matrice de confusion")
    vizstyle.styled_heatmap(
        data=confusion_matrix,
        title="Matrice de confusion - Classification",
        xlabel="Prédiction",
        ylabel="Vérité",
        xticklabels=classes,
        yticklabels=classes,
        cmap='YlGnBu',
        annot=True,
        fmt='d'
    )
    
    # Données temporelles (heatmap calendrier)
    months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin',
              'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']
    years = ['2021', '2022', '2023', '2024']
    sales_data = np.random.randint(50, 200, (4, 12))
    
    print("\n5.3 - Évolution temporelle (années × mois)")
    vizstyle.styled_heatmap(
        data=sales_data,
        title="Ventes mensuelles par année",
        xlabel="Mois",
        ylabel="Année",
        xticklabels=months,
        yticklabels=years,
        cmap='RdYlGn',
        annot=True,
        fmt='d'
    )


def example_6_styled_box():
    """Exemple 6: Boîtes à moustaches"""
    print("\n" + "=" * 60)
    print("Exemple 6: Boîtes à moustaches")
    print("=" * 60)
    
    # Comparaison de groupes
    np.random.seed(42)
    groupe_A = np.random.normal(100, 15, 200)
    groupe_B = np.random.normal(110, 20, 200)
    groupe_C = np.random.normal(95, 12, 200)
    groupe_D = np.random.normal(105, 18, 200)
    
    print("\n6.1 - Comparaison de plusieurs groupes (vertical)")
    vizstyle.styled_box(
        data=[groupe_A, groupe_B, groupe_C, groupe_D],
        labels=['Groupe A', 'Groupe B', 'Groupe C', 'Groupe D'],
        title="Comparaison des performances par groupe",
        ylabel="Score"
    )
    
    # Orientation horizontale
    print("\n6.2 - Boîtes à moustaches horizontales")
    vizstyle.styled_box(
        data=[groupe_A, groupe_B, groupe_C, groupe_D],
        labels=['A', 'B', 'C', 'D'],
        title="Distributions des scores (horizontal)",
        xlabel="Score",
        horizontal=True
    )
    
    # Avant/Après traitement
    avant = np.random.normal(75, 10, 150)
    apres = avant + np.random.normal(15, 5, 150)
    
    print("\n6.3 - Comparaison avant/après")
    vizstyle.styled_box(
        data=[avant, apres],
        labels=['Avant traitement', 'Après traitement'],
        title="Effet du traitement sur les scores",
        ylabel="Score",
        color=['#D81159', '#06A77D']
    )


def example_7_comprehensive():
    """Exemple 7: Analyse complète avec tous les graphiques"""
    print("\n" + "=" * 60)
    print("Exemple 7: Analyse complète d'un dataset")
    print("=" * 60)
    
    # Générer des données simulées pour une entreprise
    np.random.seed(42)
    
    # Données mensuelles sur 2 ans
    months = np.arange(1, 25)
    ventes = 1000 + months * 50 + np.random.normal(0, 100, 24)
    couts = 600 + months * 20 + np.random.normal(0, 50, 24)
    profit = ventes - couts
    
    print("\n7.1 - Évolution temporelle")
    vizstyle.styled_line(
        x=months,
        y=[ventes, couts, profit],
        title="Évolution des métriques financières (24 mois)",
        xlabel="Mois",
        ylabel="Montant (k€)",
        label=['Ventes', 'Coûts', 'Profit']
    )
    
    # Distribution des profits
    print("\n7.2 - Distribution du profit mensuel")
    vizstyle.styled_histogram(
        data=profit,
        bins=15,
        title="Distribution du profit mensuel",
        xlabel="Profit (k€)",
        kde=True
    )
    
    # Comparaison par année
    year1 = profit[:12]
    year2 = profit[12:]
    
    print("\n7.3 - Comparaison des profits par année")
    vizstyle.styled_box(
        data=[year1, year2],
        labels=['Année 1', 'Année 2'],
        title="Distribution des profits annuels",
        ylabel="Profit mensuel (k€)"
    )
    
    # Performance par trimestre
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    q_profit_y1 = [year1[:3].mean(), year1[3:6].mean(), 
                   year1[6:9].mean(), year1[9:].mean()]
    q_profit_y2 = [year2[:3].mean(), year2[3:6].mean(), 
                   year2[6:9].mean(), year2[9:].mean()]
    
    print("\n7.4 - Profit moyen par trimestre")
    vizstyle.styled_bar(
        x=quarters,
        y=[q_profit_y1, q_profit_y2],
        title="Profit moyen par trimestre",
        xlabel="Trimestre",
        ylabel="Profit moyen (k€)",
        labels=['Année 1', 'Année 2']
    )
    
    print("\n" + "=" * 60)
    print("Analyse terminée avec succès!")
    print("=" * 60)


def main():
    """Fonction principale pour exécuter tous les exemples"""
    print("\n")
    print("*" * 60)
    print("*" + " " * 58 + "*")
    print("*" + " " * 10 + "VIZSTYLE - EXEMPLES DE VISUALISATION" + " " * 11 + "*")
    print("*" + " " * 58 + "*")
    print("*" * 60)
    print("\nCe script démontre toutes les fonctionnalités de VizStyle")
    print("Appuyez sur Entrée pour continuer vers le prochain exemple...")
    input()
    
    try:
        # Exécuter tous les exemples
        example_1_styled_line()
        input("\nAppuyez sur Entrée pour continuer...")
        
        example_2_styled_scatter()
        input("\nAppuyez sur Entrée pour continuer...")
        
        example_3_styled_bar()
        input("\nAppuyez sur Entrée pour continuer...")
        
        example_4_styled_histogram()
        input("\nAppuyez sur Entrée pour continuer...")
        
        example_5_styled_heatmap()
        input("\nAppuyez sur Entrée pour continuer...")
        
        example_6_styled_box()
        input("\nAppuyez sur Entrée pour continuer...")
        
        example_7_comprehensive()
        
        print("\n\n" + "=" * 60)
        print("TOUS LES EXEMPLES ONT ÉTÉ EXÉCUTÉS AVEC SUCCÈS! ✓")
        print("=" * 60)
        print("\nMerci d'avoir testé VizStyle!")
        print("Pour plus d'informations, consultez le README.md")
        
    except KeyboardInterrupt:
        print("\n\nExemples interrompus par l'utilisateur.")
    except Exception as e:
        print(f"\n\nErreur lors de l'exécution: {e}")
        raise


if __name__ == "__main__":
    main()
