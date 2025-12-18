"""
VizStyle - Bibliothèque de visualisation Python avec style personnalisé
=====================================================================

Une bibliothèque de visualisation élégante avec un style cohérent et moderne.

Fonctions disponibles:
- styled_line: Graphique en ligne
- styled_scatter: Nuage de points
- styled_bar: Graphique en barres
- styled_histogram: Histogramme
- styled_heatmap: Carte de chaleur
- styled_box: Boîte à moustaches

Auteur: sidi
Version: 1.0.0
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import rcParams

# Configuration du style global
STYLE_CONFIG = {
    'colors': {
        'primary': '#2E86AB',      # Bleu principal
        'secondary': '#A23B72',    # Violet
        'tertiary': '#F18F01',     # Orange
        'success': '#06A77D',      # Vert
        'warning': '#D81159',      # Rose/Rouge
        'info': '#73D2DE',         # Bleu clair
        'palette': ['#2E86AB', '#A23B72', '#F18F01', '#06A77D', '#D81159', '#73D2DE']
    },
    'fonts': {
        'title': 16,
        'label': 12,
        'tick': 10
    },
    'lines': {
        'width': 2.5,
        'marker_size': 8
    },
    'figure': {
        'figsize': (10, 6),
        'dpi': 100,
        'facecolor': '#F8F9FA',
        'edgecolor': 'none'
    },
    'axes': {
        'facecolor': '#FFFFFF',
        'edgecolor': '#CCCCCC',
        'linewidth': 1.5,
        'grid_alpha': 0.3,
        'grid_color': '#DDDDDD'
    }
}


def _apply_style(ax, title=None, xlabel=None, ylabel=None):
    """
    Applique le style personnalisé aux axes.
    
    Parameters:
    -----------
    ax : matplotlib.axes.Axes
        Les axes à styliser
    title : str, optional
        Titre du graphique
    xlabel : str, optional
        Label de l'axe X
    ylabel : str, optional
        Label de l'axe Y
    """
    # Fond et bordures
    ax.set_facecolor(STYLE_CONFIG['axes']['facecolor'])
    for spine in ax.spines.values():
        spine.set_edgecolor(STYLE_CONFIG['axes']['edgecolor'])
        spine.set_linewidth(STYLE_CONFIG['axes']['linewidth'])
    
    # Grille
    ax.grid(True, alpha=STYLE_CONFIG['axes']['grid_alpha'], 
            color=STYLE_CONFIG['axes']['grid_color'], linestyle='--', linewidth=1)
    ax.set_axisbelow(True)
    
    # Titres et labels
    if title:
        ax.set_title(title, fontsize=STYLE_CONFIG['fonts']['title'], 
                    fontweight='bold', pad=20, color='#333333')
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=STYLE_CONFIG['fonts']['label'], 
                     fontweight='600', color='#555555')
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=STYLE_CONFIG['fonts']['label'], 
                     fontweight='600', color='#555555')
    
    # Ticks
    ax.tick_params(labelsize=STYLE_CONFIG['fonts']['tick'], colors='#666666')


def styled_line(x, y, title=None, xlabel=None, ylabel=None, 
                label=None, color=None, figsize=None, show=True):
    """
    Crée un graphique en ligne avec le style personnalisé.
    
    Parameters:
    -----------
    x : array-like
        Valeurs de l'axe X
    y : array-like or list of array-like
        Valeurs de l'axe Y (peut être multiple pour plusieurs lignes)
    title : str, optional
        Titre du graphique
    xlabel : str, optional
        Label de l'axe X
    ylabel : str, optional
        Label de l'axe Y
    label : str or list of str, optional
        Label(s) pour la légende
    color : str or list of str, optional
        Couleur(s) personnalisée(s)
    figsize : tuple, optional
        Taille de la figure (largeur, hauteur)
    show : bool, default=True
        Afficher le graphique immédiatement
        
    Returns:
    --------
    fig, ax : tuple
        Figure et axes matplotlib
        
    Example:
    --------
    >>> import vizstyle
    >>> vizstyle.styled_line([1, 2, 3], [4, 2, 5], title="Ma courbe")
    """
    figsize = figsize or STYLE_CONFIG['figure']['figsize']
    fig, ax = plt.subplots(figsize=figsize, dpi=STYLE_CONFIG['figure']['dpi'])
    fig.patch.set_facecolor(STYLE_CONFIG['figure']['facecolor'])
    
    # Gérer plusieurs courbes
    if isinstance(y[0], (list, np.ndarray)) and len(y) > 1 and not isinstance(y, np.ndarray):
        # Plusieurs courbes
        colors = color if color else STYLE_CONFIG['colors']['palette']
        labels = label if label else [f'Série {i+1}' for i in range(len(y))]
        
        for i, y_data in enumerate(y):
            c = colors[i % len(colors)] if isinstance(colors, list) else colors
            l = labels[i] if isinstance(labels, list) else labels
            ax.plot(x, y_data, color=c, linewidth=STYLE_CONFIG['lines']['width'],
                   marker='o', markersize=STYLE_CONFIG['lines']['marker_size']*0.7,
                   label=l, alpha=0.9)
        ax.legend(frameon=True, fancybox=True, shadow=True, 
                 fontsize=STYLE_CONFIG['fonts']['tick'])
    else:
        # Une seule courbe
        c = color or STYLE_CONFIG['colors']['primary']
        ax.plot(x, y, color=c, linewidth=STYLE_CONFIG['lines']['width'],
               marker='o', markersize=STYLE_CONFIG['lines']['marker_size']*0.7,
               label=label, alpha=0.9)
        if label:
            ax.legend(frameon=True, fancybox=True, shadow=True,
                     fontsize=STYLE_CONFIG['fonts']['tick'])
    
    _apply_style(ax, title, xlabel, ylabel)
    plt.tight_layout()
    
    if show:
        plt.show()
    
    return fig, ax


def styled_scatter(x, y, title=None, xlabel=None, ylabel=None,
                   label=None, color=None, size=None, figsize=None, show=True):
    """
    Crée un nuage de points avec le style personnalisé.
    
    Parameters:
    -----------
    x : array-like
        Valeurs de l'axe X
    y : array-like
        Valeurs de l'axe Y
    title : str, optional
        Titre du graphique
    xlabel : str, optional
        Label de l'axe X
    ylabel : str, optional
        Label de l'axe Y
    label : str, optional
        Label pour la légende
    color : str or array-like, optional
        Couleur(s) des points
    size : int or array-like, optional
        Taille(s) des points
    figsize : tuple, optional
        Taille de la figure
    show : bool, default=True
        Afficher le graphique immédiatement
        
    Returns:
    --------
    fig, ax : tuple
        Figure et axes matplotlib
        
    Example:
    --------
    >>> import vizstyle
    >>> vizstyle.styled_scatter([1, 2, 3, 4], [2, 4, 3, 5], title="Nuage de points")
    """
    figsize = figsize or STYLE_CONFIG['figure']['figsize']
    fig, ax = plt.subplots(figsize=figsize, dpi=STYLE_CONFIG['figure']['dpi'])
    fig.patch.set_facecolor(STYLE_CONFIG['figure']['facecolor'])
    
    c = color if color is not None else STYLE_CONFIG['colors']['primary']
    s = size if size is not None else STYLE_CONFIG['lines']['marker_size']**2
    
    scatter = ax.scatter(x, y, c=c, s=s, alpha=0.7, 
                        edgecolors='white', linewidth=1.5, label=label)
    
    if label:
        ax.legend(frameon=True, fancybox=True, shadow=True,
                 fontsize=STYLE_CONFIG['fonts']['tick'])
    
    _apply_style(ax, title, xlabel, ylabel)
    plt.tight_layout()
    
    if show:
        plt.show()
    
    return fig, ax


def styled_bar(x, y, title=None, xlabel=None, ylabel=None,
               labels=None, color=None, horizontal=False, figsize=None, show=True):
    """
    Crée un graphique en barres avec le style personnalisé.
    
    Parameters:
    -----------
    x : array-like
        Catégories ou positions
    y : array-like or list of array-like
        Hauteurs des barres (peut être multiple pour barres groupées)
    title : str, optional
        Titre du graphique
    xlabel : str, optional
        Label de l'axe X
    ylabel : str, optional
        Label de l'axe Y
    labels : str or list of str, optional
        Labels pour la légende (barres groupées)
    color : str or list of str, optional
        Couleur(s) des barres
    horizontal : bool, default=False
        Créer des barres horizontales
    figsize : tuple, optional
        Taille de la figure
    show : bool, default=True
        Afficher le graphique immédiatement
        
    Returns:
    --------
    fig, ax : tuple
        Figure et axes matplotlib
        
    Example:
    --------
    >>> import vizstyle
    >>> vizstyle.styled_bar(['A', 'B', 'C'], [10, 25, 15], title="Graphique en barres")
    """
    figsize = figsize or STYLE_CONFIG['figure']['figsize']
    fig, ax = plt.subplots(figsize=figsize, dpi=STYLE_CONFIG['figure']['dpi'])
    fig.patch.set_facecolor(STYLE_CONFIG['figure']['facecolor'])
    
    # Vérifier si y est une liste de listes (barres groupées)
    is_grouped = isinstance(y, list) and len(y) > 0 and isinstance(y[0], (list, np.ndarray))
    
    if is_grouped:
        # Barres groupées
        n_groups = len(y)
        colors = color if color else STYLE_CONFIG['colors']['palette'][:n_groups]
        labels_list = labels if labels else [f'Groupe {i+1}' for i in range(n_groups)]
        
        x_pos = np.arange(len(x))
        width = 0.8 / n_groups
        
        for i, y_data in enumerate(y):
            offset = (i - n_groups/2 + 0.5) * width
            c = colors[i] if isinstance(colors, list) else colors
            l = labels_list[i] if isinstance(labels_list, list) else labels_list
            
            if horizontal:
                ax.barh(x_pos + offset, y_data, width, label=l, color=c, 
                       alpha=0.8, edgecolor='white', linewidth=1.5)
            else:
                ax.bar(x_pos + offset, y_data, width, label=l, color=c,
                      alpha=0.8, edgecolor='white', linewidth=1.5)
        
        if horizontal:
            ax.set_yticks(x_pos)
            ax.set_yticklabels(x)
        else:
            ax.set_xticks(x_pos)
            ax.set_xticklabels(x)
        
        ax.legend(frameon=True, fancybox=True, shadow=True,
                 fontsize=STYLE_CONFIG['fonts']['tick'])
    else:
        # Barres simples
        c = color if color else STYLE_CONFIG['colors']['primary']
        
        if horizontal:
            bars = ax.barh(x, y, color=c, alpha=0.8, 
                          edgecolor='white', linewidth=1.5)
        else:
            bars = ax.bar(x, y, color=c, alpha=0.8,
                         edgecolor='white', linewidth=1.5)
    
    _apply_style(ax, title, xlabel, ylabel)
    plt.tight_layout()
    
    if show:
        plt.show()
    
    return fig, ax


def styled_histogram(data, bins=30, title=None, xlabel=None, ylabel=None,
                     color=None, kde=True, figsize=None, show=True):
    """
    Crée un histogramme avec le style personnalisé.
    
    Parameters:
    -----------
    data : array-like
        Données à visualiser
    bins : int, default=30
        Nombre de bins
    title : str, optional
        Titre du graphique
    xlabel : str, optional
        Label de l'axe X
    ylabel : str, optional
        Label de l'axe Y
    color : str, optional
        Couleur des barres
    kde : bool, default=True
        Ajouter une courbe de densité (KDE)
    figsize : tuple, optional
        Taille de la figure
    show : bool, default=True
        Afficher le graphique immédiatement
        
    Returns:
    --------
    fig, ax : tuple
        Figure et axes matplotlib
        
    Example:
    --------
    >>> import vizstyle
    >>> import numpy as np
    >>> data = np.random.normal(0, 1, 1000)
    >>> vizstyle.styled_histogram(data, title="Distribution")
    """
    figsize = figsize or STYLE_CONFIG['figure']['figsize']
    fig, ax = plt.subplots(figsize=figsize, dpi=STYLE_CONFIG['figure']['dpi'])
    fig.patch.set_facecolor(STYLE_CONFIG['figure']['facecolor'])
    
    c = color or STYLE_CONFIG['colors']['primary']
    
    # Histogramme
    n, bins_edges, patches = ax.hist(data, bins=bins, color=c, alpha=0.7,
                                      edgecolor='white', linewidth=1.5, density=kde)
    
    # KDE
    if kde:
        from scipy import stats
        density = stats.gaussian_kde(data)
        xs = np.linspace(data.min(), data.max(), 200)
        ax.plot(xs, density(xs), color=STYLE_CONFIG['colors']['secondary'],
               linewidth=STYLE_CONFIG['lines']['width'], label='Densité (KDE)')
        ax.legend(frameon=True, fancybox=True, shadow=True,
                 fontsize=STYLE_CONFIG['fonts']['tick'])
    
    ylabel = ylabel or ('Densité' if kde else 'Fréquence')
    _apply_style(ax, title, xlabel, ylabel)
    plt.tight_layout()
    
    if show:
        plt.show()
    
    return fig, ax


def styled_heatmap(data, title=None, xlabel=None, ylabel=None,
                   xticklabels=None, yticklabels=None, cmap=None,
                   annot=True, fmt='.2f', figsize=None, show=True):
    """
    Crée une carte de chaleur avec le style personnalisé.
    
    Parameters:
    -----------
    data : array-like (2D)
        Matrice de données à visualiser
    title : str, optional
        Titre du graphique
    xlabel : str, optional
        Label de l'axe X
    ylabel : str, optional
        Label de l'axe Y
    xticklabels : list, optional
        Labels pour l'axe X
    yticklabels : list, optional
        Labels pour l'axe Y
    cmap : str, optional
        Palette de couleurs
    annot : bool, default=True
        Annoter les cellules avec les valeurs
    fmt : str, default='.2f'
        Format des annotations
    figsize : tuple, optional
        Taille de la figure
    show : bool, default=True
        Afficher le graphique immédiatement
        
    Returns:
    --------
    fig, ax : tuple
        Figure et axes matplotlib
        
    Example:
    --------
    >>> import vizstyle
    >>> import numpy as np
    >>> data = np.random.rand(5, 5)
    >>> vizstyle.styled_heatmap(data, title="Carte de chaleur")
    """
    figsize = figsize or (10, 8)
    fig, ax = plt.subplots(figsize=figsize, dpi=STYLE_CONFIG['figure']['dpi'])
    fig.patch.set_facecolor(STYLE_CONFIG['figure']['facecolor'])
    
    cmap = cmap or 'RdYlBu_r'
    
    # Gérer les tick labels (seaborn n'accepte pas None)
    xtick = xticklabels if xticklabels is not None else True
    ytick = yticklabels if yticklabels is not None else True
    
    # Créer la heatmap avec seaborn
    sns.heatmap(data, annot=annot, fmt=fmt, cmap=cmap, 
               xticklabels=xtick, yticklabels=ytick,
               cbar_kws={'shrink': 0.8}, linewidths=0.5, linecolor='white',
               ax=ax)
    
    # Appliquer le style (sans la grille pour les heatmaps)
    ax.set_facecolor(STYLE_CONFIG['axes']['facecolor'])
    
    if title:
        ax.set_title(title, fontsize=STYLE_CONFIG['fonts']['title'],
                    fontweight='bold', pad=20, color='#333333')
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=STYLE_CONFIG['fonts']['label'],
                     fontweight='600', color='#555555')
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=STYLE_CONFIG['fonts']['label'],
                     fontweight='600', color='#555555')
    
    ax.tick_params(labelsize=STYLE_CONFIG['fonts']['tick'], colors='#666666')
    plt.tight_layout()
    
    if show:
        plt.show()
    
    return fig, ax


def styled_box(data, labels=None, title=None, xlabel=None, ylabel=None,
               color=None, horizontal=False, figsize=None, show=True):
    """
    Crée une boîte à moustaches avec le style personnalisé.
    
    Parameters:
    -----------
    data : array-like or list of array-like
        Données à visualiser (peut être multiple pour plusieurs boîtes)
    labels : list of str, optional
        Labels pour chaque boîte
    title : str, optional
        Titre du graphique
    xlabel : str, optional
        Label de l'axe X
    ylabel : str, optional
        Label de l'axe Y
    color : str or list, optional
        Couleur(s) des boîtes
    horizontal : bool, default=False
        Orientation horizontale
    figsize : tuple, optional
        Taille de la figure
    show : bool, default=True
        Afficher le graphique immédiatement
        
    Returns:
    --------
    fig, ax : tuple
        Figure et axes matplotlib
        
    Example:
    --------
    >>> import vizstyle
    >>> import numpy as np
    >>> data = [np.random.normal(0, 1, 100), np.random.normal(1, 1.5, 100)]
    >>> vizstyle.styled_box(data, labels=['Groupe A', 'Groupe B'], title="Comparaison")
    """
    figsize = figsize or STYLE_CONFIG['figure']['figsize']
    fig, ax = plt.subplots(figsize=figsize, dpi=STYLE_CONFIG['figure']['dpi'])
    fig.patch.set_facecolor(STYLE_CONFIG['figure']['facecolor'])
    
    # S'assurer que data est une liste de listes
    if not isinstance(data[0], (list, np.ndarray)):
        data = [data]
    
    colors = color if color else STYLE_CONFIG['colors']['palette']
    if isinstance(colors, str):
        colors = [colors]
    
    # Créer les boxplots
    bp = ax.boxplot(data, labels=labels, patch_artist=True, 
                    vert=not horizontal, widths=0.6,
                    boxprops=dict(facecolor=colors[0], alpha=0.7, linewidth=1.5),
                    whiskerprops=dict(linewidth=1.5),
                    capprops=dict(linewidth=1.5),
                    medianprops=dict(color='#D81159', linewidth=2.5),
                    flierprops=dict(marker='o', markerfacecolor=colors[0], 
                                   markersize=6, alpha=0.5))
    
    # Colorer chaque boîte différemment si plusieurs
    if len(data) > 1:
        for patch, color in zip(bp['boxes'], colors * (len(data) // len(colors) + 1)):
            patch.set_facecolor(color)
    
    _apply_style(ax, title, xlabel, ylabel)
    plt.tight_layout()
    
    if show:
        plt.show()
    
    return fig, ax


# Exporter les fonctions principales
__all__ = [
    'styled_line',
    'styled_scatter',
    'styled_bar',
    'styled_histogram',
    'styled_heatmap',
    'styled_box',
    'STYLE_CONFIG'
]

__version__ = '1.0.0'
