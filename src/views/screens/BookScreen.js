import React, { useState } from 'react';
import { View, Text, TextInput, StyleSheet, TouchableOpacity,SafeAreaView} from 'react-native';
import COLORS from '../../consts/colors';
import Icon from 'react-native-vector-icons/MaterialIcons';
import Slider from './Slider';

const BookScreen = ({navigation}) => {
  const image = [
    'https://assets.hotelaparis.com/uploads/pictures/000/043/953/Chambre-3-6.jpg',
    'https://www.yonder.fr/sites/default/files/styles/lg-insert/public/contenu/destinations/5%20Codet%20chambre%20%C2%A9%20Antoine%20Schramm_0.jpg?itok=jv3m9LdX',
    'https://www.lyon-entreprises.com/wp-content/uploads/2022/05/img-chambres-decorer-points-1024x683.jpg',
  ];



  const [checkInDate, setCheckInDate] = useState('');
  const [checkOutDate, setCheckOutDate] = useState('');
  const [guests, setGuests] = useState('');

  const handleCheckInDateChange = (text) => {
    setCheckInDate(text);
  };

  const handleCheckOutDateChange = (text) => {
    setCheckOutDate(text);
  };

  const handleGuestsChange = (text) => {
    setGuests(text);
  };

  const handleSubmit = () => {
    // Handle form submission here
  };

  return (
    <SafeAreaView style={{flex: 1, backgroundColor: COLORS.white}}>
      <View style={style.header}>
        <View style={{paddingBottom: 15}}>
          <Text style={{fontSize: 30, fontWeight: 'bold', color: COLORS.primary}}>
            Hotel Gazelle
          </Text>
        </View>
        <Icon name="person-outline" size={38} color={COLORS.grey} />
      </View>
      {/* <Dashboard/> */}
      <View >
        <Text style={style.text}>choose a task</Text>
        <TouchableOpacity
          style={style.button}
          onPress={() => navigation.navigate('Chambres')}
        >
          <Text style={style.buttonText}>manage rooms</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={style.button}
          onPress={() => navigation.navigate('Reservations')}
        >
          <Text style={style.buttonText}>manage reservations</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={style.button}
        //   onPress={() => navigation.navigate('Clients')}
        >
          <Text style={style.buttonText}>manage clients</Text>
        </TouchableOpacity>
        <Slider images={image}  />
      </View>
      

    </SafeAreaView>   

  )
  

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
    marginTop:25,
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
export default BookScreen;
