import numpy as np

def pagerank(matrix, d=0.85, max_iterations=100, tol=1e-6):
    n = matrix.shape[0]
    # 初始化PageRank值
    pr = np.ones(n) / n
    # 轉置矩陣
    matrix_t = matrix.T
    for _ in range(max_iterations):
        pr_new = np.ones(n) * (1 - d) / n + d * matrix_t.dot(pr / matrix.sum(axis=1))
        # 判斷是否收斂
        if np.linalg.norm(pr_new - pr) < tol:
            break
        pr = pr_new
    return pr

# 測試PageRank演算法
if __name__ == "__main__":
    # 網頁連結矩陣（行表示鏈出，列表示鏈入）
    link_matrix = np.array([[0, 0, 1, 0],
                            [1, 0, 0, 1],
                            [0, 1, 0, 0],
                            [0, 1, 1, 0]])
    pr = pagerank(link_matrix)
    print(f"PageRank值: {pr}")
