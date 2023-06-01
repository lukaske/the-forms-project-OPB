import { AuthenticationTitle } from '../src/components/AuthenticationTitle/AuthenticationTitle';
import {Container} from '@mantine/core';
export default function HomePage() {
  return (
    <>
    <Container style={{maxWidth: '71rem'}}>
    <iframe style={{width: '100%', height: '90vh', justifyContent: 'center'}} srcDoc="<html>
  <head>
    <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css'>
    <link rel='stylesheet' href='https://cdn.form.io/formiojs/formio.full.min.css'>
    <script src='https://cdn.form.io/formiojs/formio.full.min.js'></script>
    <script type='text/javascript'>
      window.onload = function() {
        Formio.builder(document.getElementById('builder'), {}, {});
      };
    </script>
  </head>
  <body>
    <div id='builder'></div>
  </body>
</html>
"> </iframe>

      </Container>
    </>
  );
}
