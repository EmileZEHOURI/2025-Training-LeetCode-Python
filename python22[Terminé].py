class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        result = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Parcours de gauche à droite
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1  # On déplace la limite supérieure vers le bas

            # Parcours de haut en bas
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # On déplace la limite droite vers la gauche

            if top <= bottom:
                # Parcours de droite à gauche
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1  # On déplace la limite inférieure vers le haut

            if left <= right:
                # Parcours de bas en haut
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # On déplace la limite gauche vers la droite

        return result

# Exemple d'utilisation :
matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution = Solution()
result = solution.spiralOrder(matrix)
print(result)
