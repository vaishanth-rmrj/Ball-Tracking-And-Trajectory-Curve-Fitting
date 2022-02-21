
import numpy as np

class ParabolaTrajectoryFinder:

    def __init__(self, data):
        # initialinzing the data to fit
        self.data = data


    def calculate_parabola_pts(self, x, y):
        """
        method to calculate parabola curve points for the given data

        Args:
            x (list): x data
            y (list): y data

        Returns:
            list: all the predicted y points for the corresponding x data
        """

        y_pred = list()
        # calculating equation values
        xy =  []
        x2y = []
        x2 =  []
        x3 =  []
        x4 =  []

        # calculating respective equation values
        for i in range(0, len(x)):
            xy.append(x[i]*y[i])
            x2y.append(x[i]*x[i]*y[i])
            x2.append(x[i]*x[i])
            x3.append(x[i]*x[i]*x[i])
            x4.append(x[i]*x[i]*x[i]*x[i])

        # # calculating the sum of respective equation values
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(xy)
        sum_x2y = sum(x2y)
        sum_x2 = sum(x2)
        sum_x3 = sum(x3)
        sum_x4 = sum(x4)

        n = len(x)
        # calculating augmented matrix for solving parabola system of equations
        aug_matrix = np.matrix([[sum_x2, sum_x, n, sum_y], [sum_x3, sum_x2, sum_x, sum_xy], [sum_x4, sum_x3, sum_x2, sum_x2y]])

        rows, cols = aug_matrix.shape
        for col in range(cols-1):
            for row in range(col+1, rows):        
                aug_matrix[row,:] = aug_matrix[row,:] - ((aug_matrix[row,col]/aug_matrix[col,col])*aug_matrix[col,:])

        c = aug_matrix[2,3]/aug_matrix[2,2] 
        b = (aug_matrix[1,3] - (aug_matrix[1,2]*c))/aug_matrix[1,1]
        a = (aug_matrix[0,3]- (aug_matrix[0,2]*c) - (aug_matrix[0,1]*b))/ aug_matrix[0,0]

        # calculting new y values using the calculated curve co-efficients
        for x_pt in x:
            y_pred.append(a*(x_pt**2) + b*(x_pt) + c)

        return y_pred

    def get_curve_data(self):
        """
        method to return predicted x and y predicted values

        Returns:
            (x, y_predicted)
        """

        x_data = list()
        y_data = list()

        # seperating x and y data into different lists
        for point in self.data:
            x_data.append(int(point[0]))
            y_data.append(int(point[1]))

        return x_data, self.calculate_parabola_pts(x_data, y_data)

       

        