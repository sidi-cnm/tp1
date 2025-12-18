# Guide d'Installation Rapide - VizStyle

## 📦 Installation

### Méthode 1: Installation en mode développement (recommandée pour tester)

```bash
# Depuis le répertoire vizstyle/
pip install -e .
```

Cette méthode installe la bibliothèque en mode "editable", permettant de modifier le code sans réinstaller.

### Méthode 2: Installation standard

```bash
# Depuis le répertoire vizstyle/
pip install .
```

### Méthode 3: Installation depuis un fichier wheel

```bash
# D'abord, créer le package
python setup.py sdist bdist_wheel

# Ensuite, installer
pip install dist/vizstyle-1.0.0-py3-none-any.whl
```

## ✅ Vérification de l'installation

```python
# Tester l'import
import vizstyle
print(f"VizStyle version {vizstyle.__version__} installée avec succès!")

# Test rapide
vizstyle.styled_line([1, 2, 3], [4, 2, 5], title="Test")
```

## 🚀 Premier exemple

```python
import vizstyle
import numpy as np

# Créer des données
x = np.linspace(0, 10, 50)
y = np.sin(x)

# Créer un graphique stylisé
vizstyle.styled_line(
    x=x,
    y=y,
    title="Ma première visualisation avec VizStyle",
    xlabel="x",
    ylabel="sin(x)"
)
```

## 📚 Exécuter les exemples

```bash
# Depuis le répertoire vizstyle/
python examples.py
```

## 🔧 Dépannage

### Erreur: Module not found

Si vous obtenez `ModuleNotFoundError: No module named 'vizstyle'`:

1. Vérifiez que vous êtes dans le bon environnement Python
2. Réinstallez la bibliothèque: `pip install -e .`
3. Vérifiez l'installation: `pip list | grep vizstyle`

### Erreur: Missing dependencies

Si des dépendances manquent:

```bash
pip install -r requirements.txt
```

### Problèmes d'affichage

Si les graphiques ne s'affichent pas:

- Assurez-vous d'avoir un backend matplotlib configuré
- Ajoutez `import matplotlib; matplotlib.use('TkAgg')` avant d'importer vizstyle

## 📖 Documentation complète

Consultez le fichier README.md pour la documentation complète avec tous les exemples.

## 🆘 Besoin d'aide?

- Consultez le README.md
- Regardez examples.py pour des cas d'utilisation
- Vérifiez que toutes les dépendances sont installées

---

Bon codage avec VizStyle! 📊✨
