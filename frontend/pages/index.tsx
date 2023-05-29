import { Welcome } from '../components/Welcome/Welcome';
import { ColorSchemeToggle } from '../components/ColorSchemeToggle/ColorSchemeToggle';
import { HeroImageRight } from '../components/HeroImageRight/HeroImageRight';
import { FeaturesTitle } from '../components/FeaturesTitle/FeaturesTitle';
import { FooterLinks } from '../components/FooterLinks/FooterLinks';
import footer from '../config/footer.json';
import { FeaturesCards } from '../components/FeaturesCards/FeaturesCards';
import { FaqSimple } from '../components/FaqSimple/FaqSimple';
import { HeroBullets } from '../components/HeroBullets/HeroBullets';

export default function HomePage() {
  return (
    <>
      <HeroImageRight />
      <FeaturesCards />
      <FaqSimple/>
      <FooterLinks {...footer.props}/>
    </>
  );
}
