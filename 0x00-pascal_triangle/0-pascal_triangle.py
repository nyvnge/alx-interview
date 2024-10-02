#!/usr/bin/python3
"""
0. Pascal's Triangle - Variation
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    
    This variation uses a different method to calculate each row.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i-1] + prev_row[i])
        
        new_row.append(1)
        triangle.append(new_row)
    
    return triangle
