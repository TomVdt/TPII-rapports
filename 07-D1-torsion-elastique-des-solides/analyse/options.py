rcParams = {
    "text.usetex": True,
    "font.family": "serif",
    "axes.labelsize": 12,
    "font.size": 12,
    "legend.fontsize": 11,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "figure.figsize": (4.5, 3.5),
    "text.latex.preamble": "\n".join([
        r"\usepackage[utf8]{inputenc}",
        r"\usepackage[T1]{fontenc}",
        r"\usepackage[detect-all,locale=FR]{siunitx}",
        r"\usepackage{mathabx}",
    ]),
    'lines.markersize': 12,
    'lines.color': 'grey',
    'scatter.marker': '+',
    'errorbar.capsize': 4,
    'savefig.bbox': 'tight',
    # 'savefig.directory': '../figures/'
}
