from mcp.server.fastmcp import FastMCP
import math

# Create an MCP server
mcp = FastMCP("Math MCP Server")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers"""
    if b == 0:
        return "Undefined (division by zero)"
    return a / b

@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Raise a number to the power of another"""
    return base ** exponent

@mcp.tool()
def factorial(n: float) -> float:
    """Calculate the factorial of a number"""
    if (n == 0):
        return 1
    return math.factorial(n)
   

@mcp.tool()
def square_root(n: float) -> float:
    """Calculate the square root of a number"""
    if n < 0:
        return "Undefined (negative number)"
    return math.sqrt(n)

@mcp.tool()
def gcd(a: float, b: float) -> float:
    """Calculate the greatest common divisor of two numbers"""
    return math.gcd(int(a), int(b))

@mcp.tool()
def cosine(angle: float) -> float:
    """Calculate the cosine of an angle in degrees"""
    return math.cos(math.radians(angle))

@mcp.tool()
def sine(angle: float) -> float:  
    """Calculate the sine of an angle in degrees"""
    return math.sin(math.radians(angle))

@mcp.tool()
def tangent(angle: float) -> float:
    """Calculate the tangent of an angle in degrees"""
    return math.tan(math.radians(angle))

@mcp.tool()
def logarithm(value: float, base: float = 10) -> float:
    """Calculate the logarithm of a value with a specified base"""
    if value <= 0 or base <= 0 or base == 1:
        return "Undefined (invalid input)"
    return math.log(value, base)

@mcp.tool()
def absolute_value(n: float) -> float:
    """Calculate the absolute value of a number"""
    return abs(n)

