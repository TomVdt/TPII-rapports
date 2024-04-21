rcParams = {
    "text.usetex": True,
    "font.family": "serif",
    "axes.labelsize": 14,
    "font.size": 14,
    "legend.fontsize": 14,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    "figure.figsize": (4.5, 3.5),
    "text.latex.preamble": "\n".join([
        r"\usepackage[utf8]{inputenc}",
        r"\usepackage[T1]{fontenc}",
        r"\usepackage[detect-all,locale=FR]{siunitx}",
        r"\usepackage{mathabx}",
    ]),
    'lines.markersize': 14,
    'lines.color': 'grey',
    'scatter.marker': '+',
    'errorbar.capsize': 4,
    'savefig.bbox': 'tight',
    # 'savefig.directory': '../figures/'
}
