using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace PythonAPIExample.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PythonController : ControllerBase
    {
        [HttpGet]
        public IActionResult GetStoredProcedureResult([FromQuery] string consulta, [FromQuery] string dbSap)
        {
            try
            {
                // Path to the Python script (ensure it's accessible from here)
                var pythonScriptPath = @"C:\UA\PythonAPIExample\scriptPY\execute_stored_procedure1.py"; // Change this path
                var pythonExePath = @"C:\Users\User\AppData\Local\Programs\Python\Python313\python.exe"; // Change this path to your Python executable path
                
                // Prepare arguments to pass to the Python script
                var startInfo = new ProcessStartInfo
                {
                    FileName = pythonExePath,
                    Arguments = $"{pythonScriptPath} {consulta} {dbSap}",
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,  // Redirect standard error as well
                    UseShellExecute = false,
                    CreateNoWindow = true
                };

                using (var process = Process.Start(startInfo))
                using (var reader = process.StandardOutput)
                using (var errorReader = process.StandardError)  // Read errors
                {
                    var result = reader.ReadToEnd();  // Capture the result from the Python script
                    var errorResult = errorReader.ReadToEnd();  // Capture any errors from the Python script

                    if (!string.IsNullOrEmpty(errorResult))
                    {
                        return StatusCode(500, $"Error from Python script: {errorResult}");
                    }

                    return Ok(result);  // Return the result as HTTP response
                }
            }
            catch (System.Exception ex)
            {
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }
    }
}
