import {
  TextInput,
  PasswordInput,
  Checkbox,
  Anchor,
  Paper,
  Title,
  Text,
  Container,
  Group,
  Button,
} from '@mantine/core';
import {useRouter} from 'next/router';
import { useForm } from '@mantine/form';

export function RegisrationTitle() {
  const push = useRouter().push;
  const form = useForm({
    initialValues: { email: '', password: '', vpassword: '', terms: true },

    // functions will be used to validate values at corresponding key
    validate: {
      email: (value) => (/^\S+@\S+$/.test(value) ? null : 'Neveljaven email naslov'),
      password: (value) => (value.length < 8 ? 'Geslo mora biti dolgo vsaj 8 znakov' : null),
      vpassword: (value, values) => value !== values.password ? 'Gesli se ne ujemata!' : null,
      terms: (value) => value ? null : 'Strinjati se morate s pogoji uporabe',

    },
  });




  return (
    <Container size={420} my={100}>
      <Title
        align="center"
        sx={(theme) => ({ fontFamily: `Greycliff CF, ${theme.fontFamily}`, fontWeight: 900 })}
      >
        Registracija
      </Title>
      <Text color="dimmed" size="sm" align="center" mt={5}>
        Že imate uporabniški račun?{' '}
        <Anchor size="sm" component="button" onClick={() => push('/login')}>
            Prijava
        </Anchor>
      </Text>

      <Paper withBorder shadow="md" p={30} mt={30} radius="md">
        <form onSubmit={form.onSubmit(console.log)}>
        <TextInput label="Email" placeholder="uporabnik@email.com" required {...form.getInputProps('email')}  />
        <PasswordInput label="Geslo" placeholder="Vaše geslo" required mt="md" {...form.getInputProps('password')} />
        <PasswordInput label="Ponovite geslo" placeholder="Ponovno vnesite geslo" required mt="md" {...form.getInputProps('vpassword')} />
        <Group position="apart" mt="lg">
          <Checkbox label="Strinjam se s pogoji uporabe" defaultChecked {...form.getInputProps('terms')} />
        </Group>

        <Button fullWidth mt="xl" type='submit'>
          Ustvari račun
        </Button>
        </form>
      </Paper>
    </Container>
  );
}
