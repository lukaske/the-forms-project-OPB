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

export function AuthenticationTitle() {
  return (
    <Container size={420} my={100}>
      <Title
        align="center"
        sx={(theme) => ({ fontFamily: `Greycliff CF, ${theme.fontFamily}`, fontWeight: 900 })}
      >
        Dobrodošli nazaj!
      </Title>
      <Text color="dimmed" size="sm" align="center" mt={5}>
        Še nimate uporabniškega računa?{' '}
        <Anchor size="sm" component="button">
            Ustvari ga
        </Anchor>
      </Text>

      <Paper withBorder shadow="md" p={30} mt={30} radius="md">
        <TextInput label="Email" placeholder="uporabnik@email.com" required />
        <PasswordInput label="Geslo" placeholder="Vaše geslo" required mt="md" />
        <Group position="apart" mt="lg">
          <Checkbox label="Zapomni si me" />
          <Anchor component="button" size="sm">
            Pozabljeno geslo?
          </Anchor>
        </Group>
        <Button fullWidth mt="xl">
          Prijava
        </Button>
      </Paper>
    </Container>
  );
}
