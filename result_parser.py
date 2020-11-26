import json
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    result_list = {}
    file_list = []
    for name in glob.glob('./results/*.json'):
        file_list.append(name)

    for file in file_list:
        with open(file) as f:
            df = json.load(f)
            for i in df:
                if i['filename'] not in result_list:
                    result_list[i['filename']] = [i['score']]
                else:
                    result_list[i['filename']].append(i['score'])

    with open('./psnr.json') as f:
        psnr = json.load(f)

    plt.figure()
    plt.xlabel('PSNR')
    plt.ylabel('MOS')
    scatter_x = []
    scatter_y = []
    for i in psnr:
        print(i['filename'])
        print(result_list[i['filename']])
        for score in result_list[i['filename']]:
            scatter_x.append(i['PSNR'])
            scatter_y.append(score)

    m = np.polyfit(scatter_x, scatter_y, 1)
    poly1d_fn = np.poly1d(m)
    plt.plot(scatter_x, scatter_y, 'b*', scatter_x, poly1d_fn(scatter_x), '--')

    sorted_keys = sorted(result_list.keys())
    avg_scores = []
    for i in sorted_keys:
        print(i)
        avg_scores.append(sum(result_list[i])/len(result_list[i]))

    print(avg_scores)

    np_array = np.array(avg_scores)
    avg_series = pd.Series(np_array)

    plt.figure()
    ax = avg_series.plot(kind='bar')
    ax.set_title('Average score')
    ax.set_ylabel('Score')
    ax.set_xticklabels(sorted_keys)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()








