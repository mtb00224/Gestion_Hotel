
import { StyleSheet,Text,TouchableOpacity,SafeAreaView } from 'react-native';
import COLORS from './consts/colors';
import Slider from './views/screens/Slider';
function ReservationScreen({ navigation }) {
    
      
    const image = [
      'https://assets.hotelaparis.com/uploads/pictures/000/043/953/Chambre-3-6.jpg',
      'https://www.yonder.fr/sites/default/files/styles/lg-insert/public/contenu/destinations/5%20Codet%20chambre%20%C2%A9%20Antoine%20Schramm_0.jpg?itok=jv3m9LdX',
      'https://www.lyon-entreprises.com/wp-content/uploads/2022/05/img-chambres-decorer-points-1024x683.jpg',
    ];

  return (
    <SafeAreaView >
      <Text style={style.text}>Reservations managings</Text>
      <TouchableOpacity
        style={style.button}
        // onPress={() => navigation.navigate('Chambres')}
      >
        <Text style={style.buttonText}>Add Resrvation</Text>
      </TouchableOpacity>
      <TouchableOpacity
        style={style.button}
        // onPress={() => navigation.navigate('Réservations')}
      >
        <Text style={style.buttonText}>List Reservation</Text>
      </TouchableOpacity>
      <TouchableOpacity
        style={style.button}
        // onPress={() => navigation.navigate('Clients')}
      >
        <Text style={style.buttonText}>Delete reservation</Text>
      </TouchableOpacity>
      <Slider images={image}  />
    </SafeAreaView>
    
  );
}

const style = StyleSheet.create({
    header: {
      marginTop: 25,
      flexDirection: 'row',
      justifyContent: 'space-between',
      paddingHorizontal: 20,
    },
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
    },
    text: {
      fontSize: 24,
      marginTop:12,
      marginLeft:15
    },
    button: {
      backgroundColor:  COLORS.primary,
      padding: 10,
      borderRadius: 5,
      marginBottom: 20,
      marginTop:35
    },
    buttonText: {
      color: '#ffffff',
      fontSize: 18,
    },
  
  })

export default ReservationScreen