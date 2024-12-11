from scripts.correlation.func.metric_df import metric_df
from scripts.correlation.func.plot_corr_regg import plot_combined_colors



lectin_binding_motif = {
    "AAL": {
        "motif": ["Fuc"],
        "termini_list": [["t"]]
    },
    "SNA": {
        "motif": ["Sia(a2-6)"],
        "termini_list": [["t"]]
    },
    "ConA": {
        "motif": ["Man"],
        "termini_list": [["t"]]
    },
    "MAL-II": {
        "motif": ["Sia(a2-3)"],
        "termini_list": [["t"]]
    },
    "PNA": {
        "motif": ["Gal(b1-3)GalNAc"],
        "termini_list": [["t", "f"]]
    },
    "CMA": {
        "motif": ["Fuc(a1-2)Gal", "GalNAc"],
        "termini_list": [["t", "f"], ["t"]]
    },
    "HPA": {
        "motif": ["GalNAc(a1-?)", "GlcNAc(b1-?)"],
        "termini_list": [["t"], ["t"]]
    }
}


metric_df_ = {}
for lectin, properties in lectin_binding_motif.items():
    print("")
    print(f"Processing lectin: {lectin}")
    print(f"Motif: {properties['motif']}")
    print(f"Termini: {properties['termini_list']}")

    metric_df_[lectin] = metric_df(lectin,properties)
    plot_combined_colors(metric_df_[lectin], lectin, properties["motif"])

