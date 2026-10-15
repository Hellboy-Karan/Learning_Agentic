from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math") # it just a server name i.e Math

@mcp.tool()
def add(a: float ,b: float) -> float:
    """Add two numbers"""
    return a+b

@mcp.tool()
def sub(a: float ,b: float) -> float:
    """Subtract two numbers"""
    return a-b

@mcp.tool()
def mul(a: float ,b: float) -> float:
    """Multiply two numbers"""
    return a*b

@mcp.tool()
def div(a: float ,b: float) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b

    #The transport="stdio" argument tells the server to:
    # Use standard input/output (stdin and stdout) to receive and respond to tool function call 

if __name__ == "__main__":
    mcp.run(transport="stdio")