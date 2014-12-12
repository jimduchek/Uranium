import numpy
import numpy.linalg
import math

from copy import deepcopy

##  Simple 3D-vector class based on numpy arrays.
#
#   This class represents a 3-dimensional vector.
class Vector(object):
    Unit_X = None
    Unit_Y = None
    Unit_Z = None

    def __init__(self,x = 0 ,y = 0,z = 0):
        self._data = numpy.array([x, y, z],dtype=numpy.float32)
    
    ##  Set the data of the vector
    #   \param x X coordinate of vector.
    #   \param y Y coordinate of vector.
    #   \param z Z coordinate of vector.
    def setData(self, x = 0,y = 0,z = 0):
        self._data = numpy.array([x,y,z],dtype=numpy.float32)
    
    ##  Get numpy array with the data
    #   \returns numpy array of length 3 holding xyz data.
    def getData(self):
        return self._data

    ##  Return the x component of this vector
    @property
    def x(self):
        return self._data[0]

    ##  Set the x component of this vector
    #   \param value The value for the x component
    def setX(self, value):
        self._data[0] = value

    ##  Return the y component of this vector
    @property
    def y(self):
        return self._data[1]

    ##  Set the y component of this vector
    #   \param value The value for the y component
    def setY(self, value):
        self._data[1] = value

    ## Return the z component of this vector
    @property
    def z(self):
        return self._data[2]

    ##  Set the z component of this vector
    #   \param value The value for the z component
    def setZ(self, value):
        self._data[2] = value
    
    ##  Get the angle from this vector to another
    def angleToVector(self, vector,):
        v0 = numpy.array(self._data, dtype=numpy.float32, copy=False)
        v1 = numpy.array(vector.getData(), dtype = numpy.float32, copy=False)
        dot = numpy.sum(v0 * v1)
        dot /= self._normalizeVector(v0) * self._normalizeVector(v1)
        return numpy.arccos(numpy.fabs(dot))
    
    
    def normalize(self):
        l = self.length()
        if l != 0:
            self._data /= l
        return self

    def getNormalized(self):
        other = deepcopy(self)
        return other.normalize()
    
    ##  Return length, i.e. Euclidean norm, of ndarray along axis.
    def _normalizeVector(self, data):
        data = numpy.array(data, dtype=numpy.float32, copy=True)
        if data.ndim == 1:
            return math.sqrt(numpy.dot(data, data))
        data *= data
        out = numpy.atleast_1d(numpy.sum(data))
        numpy.sqrt(out, out)
        return out

    def length(self):
        return numpy.linalg.norm(self._data)

    def dot(self, other):
        return numpy.dot(self._data, other._data)

    def cross(self, other):
        result = numpy.cross(self._data, other._data)
        return Vector(result[0], result[1], result[2])

    def rotated(self, matrix):
        result = Vector()
        result.setX(matrix.at(0, 0) * self._data[0] + matrix.at(1, 0) * self._data[1] + matrix.at(2, 0) * self._data[2])
        result.setY(matrix.at(0, 1) * self._data[0] + matrix.at(1, 1) * self._data[1] + matrix.at(2, 1) * self._data[2])
        result.setZ(matrix.at(0, 2) * self._data[0] + matrix.at(1, 2) * self._data[1] + matrix.at(2, 2) * self._data[2])
        return result

    def __add__(self, other):
        v = Vector(self._data[0], self._data[1], self._data[2])
        v += other
        return v

    def __iadd__(self, other):
        if type(other) is float:
            self._data[0] += other
            self._data[1] += other
            self._data[2] += other
        elif type(other) is Vector:
            self._data[0] += other._data[0]
            self._data[1] += other._data[1]
            self._data[2] += other._data[2]
        else:
            raise NotImplementedError()

        return self

    def __sub__(self, other):
        v = Vector(self._data[0], self._data[1], self._data[2])
        v -= other
        return v

    def __isub__(self, other):
        if type(other) is float:
            self._data[0] -= other
            self._data[1] -= other
            self._data[2] -= other
        elif type(other) is Vector:
            self._data[0] -= other._data[0]
            self._data[1] -= other._data[1]
            self._data[2] -= other._data[2]
        else:
            raise NotImplementedError()

        return self

    def __truediv__(self, other):
        v = Vector(self._data[0], self._data[1], self._data[2])
        v /= other
        return v

    def __itruediv__(self, other):
        if type(other) is float:
            self._data /= other
            return self
        else:
            raise NotImplementedError()

    def __neg__(self):
        self._data = -self._data
        return self

    def __pos__(self):
        self._data = +self._data
        return self

    def __repr__(self):
        return "Vector({0}, {1}, {2})".format(self._data[0], self._data[1], self._data[2])


Vector.Unit_X = Vector(1, 0, 0)
Vector.Unit_Y = Vector(0, 1, 0)
Vector.Unit_Z = Vector(0, 0, 1)
