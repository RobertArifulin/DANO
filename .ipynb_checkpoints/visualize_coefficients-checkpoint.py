# визуализация коэффициентов линейной регрессии
def visualize_coefficients(coefs, feature_names, top_n):
    """
    Функция для визуализации коэффициентов линейной регрессии.

    Параметры:
    -----------
        coefs: коэффициенты модели (model.coef_)
        feature_names: названия признаков (X_train.columns)
        top_n: вывести top_n самых положительных и top_n самых отрицательных признаков
    """
    feature_names = np.array(feature_names)
    if top_n * 2 > len(coefs):
        n_pos = len(coefs) // 2
        n_neg = len(coefs) - n_pos
    else:
        n_pos, n_neg = top_n, top_n
    # нам нужно найти индексы top_n наибольших и top_n наименьших коэффициентов
    min_coef_idxs = np.argsort(coefs)[:n_neg]
    max_coef_idxs = np.argsort(coefs)[len(coefs) - n_pos:]
    # соответствующие имена фичей
    top_feature_names = np.concatenate((feature_names[min_coef_idxs], feature_names[max_coef_idxs]))
    # отобразим на bar-графике
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.bar(np.arange(n_neg), coefs[min_coef_idxs], color=sns.xkcd_rgb['mauve'], hatch='/')
    ax.bar(np.arange(n_neg, n_neg + n_pos), coefs[max_coef_idxs], color=sns.xkcd_rgb['teal'], hatch='\\')
    ax.set_xticks(np.arange(0, n_neg + n_pos))
    ax.set_xticklabels(top_feature_names, rotation=45, ha="right", fontsize=14)
    plt.show()