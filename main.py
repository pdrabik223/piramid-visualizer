import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    root = "C:\\Users\\PC1080Ti\\Documents\\scans_all\\pyramid"
    file_path = os.path.join(root,"L1","data.mdma")
    
    df = pd.read_csv(file_path)
    local_z = np.array(df.data.to_numpy().real, copy=True)
    print(local_z)
    
    plt.imshow(
            local_z,
            cmap="Wistia",
            vmin=np.min(local_z),
            vmax=np.max(local_z),
            extent=[z.x_min, z.x_max, z.y_min, z.y_max],
            interpolation="none",
            origin="lower",
        )    
    plt.show()
    print("hello world")
    