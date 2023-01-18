<div><h1>README</h1><p>This code utilizes the OpenAI API to generate code for a class with a specified name and main function. The generated code will be written to a file with the class name and a specified file extension.</p><h2>Usage</h2><ol><li>Obtain an API key for OpenAI and save it in a text file named 'key'.</li><li>Import the AutoCode class.</li><li>Create an instance of the AutoCode class.</li><li>Use the <code>create_class</code> method to generate code for the desired class. The method takes in three parameters:<ul><li><code>class_name</code>: The name of the class to be generated.</li><li><code>class_main_function</code>: A brief description of what the class should do.</li><li><code>code_lang</code>: (Optional) The language of the code to be generated. Default is 'Python'.</li><li><code>extension</code>: (Optional) The file extension for the generated code file. Default is '.py'.</li></ul></li><li>The generated code will be written to a file with the class name and specified file extension.</li></ol><h2>Example</h2><pre><div class="bg-black mb-4 rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans"></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre-wrap hljs language-python"><span class="hljs-keyword">from</span> auto_code <span class="hljs-keyword">import</span> AutoCode

code_generator = AutoCode()
code_generator.create_class(<span class="hljs-string">"MyClass"</span>, <span class="hljs-string">"add two numbers together"</span>)
</code></div></div></pre><p>This will create a file named "myclass.py" with a class named "MyClass" that has a method that adds two numbers together in Python.</p><h2>Note</h2><p>The OpenAI API key must be in the same directory as the code.</p><h2>Limitations</h2><p>The generated code may not always be syntactically correct or efficient. It is recommended to review and test the generated code before using it in production.</p></div>