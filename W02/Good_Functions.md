<h3 id="func_design">Function Design</h3>
    <p>What are the properties of a good function?</p>
    <p>There are many things to consider when writing a function, and
      many authors have written about design concepts that make functions
      easier to understand and less error prone. In future courses at
      BYU-Idaho, you will study some of these design concepts. For
      CSE&nbsp;111, the following list contains a few properties that you
      should incorporate into your functions.</p>
    <ul class="long">
      <li>
        <div>A good function is understandable by other programmers.
          One way to make a function understandable is to write a
          documentation string at the top of the function that describes
          the function, its parameters, and its return value. Another way
          to make a function understandable is to write comments in the
          body of the function as needed.</div>
      </li>
      <li>
        <div>A good function performs a single task that the
          programmer can describe, and the function’s name matches its
          task.</div>
      </li>
      <li>
        <div>A good function is relatively short, perhaps fewer than
          20 lines of code.</div>
      </li>
      <li>
        <div>A good function has as few decision points
          (<code>if</code> statements and loops) as possible. Too many
          decision points in a function make a function error prone and
          difficult to test.</div>
      </li>
      <li>
        <div>A good function is as reusable as possible. Functions
          that use parameters and return a result are more reusable than
          functions that get input from a user and print results to a
          terminal window.</div>
      </li>
    </ul>
    <p>As you read the sample code in CSE&nbsp;111, observe how the
      sample functions fit these good properties, and as you write
      programs for CSE&nbsp;111, do your best to write functions that have
      these good properties.</p>